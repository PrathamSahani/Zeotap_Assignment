import ast
import operator
from django.shortcuts import render
from .models import ASTNode

OPERATORS = {
    'AND': lambda x, y: x and y,  
    'OR': lambda x, y: x or y,    
    '>': operator.gt,             
    '<': operator.lt,             
    '=': operator.eq,            
}

def create_rule(rule_string):
    tokens = rule_string.replace('(', '').replace(')', '').split()

    if len(tokens) < 3:
        raise ValueError("Invalid rule format. Expecting something like 'age > 30'")

    left_operand = tokens[0]
    root_operator = tokens[1]  
    right_operand = tokens[2]

    root = ASTNode.objects.create(type='operator', value=root_operator, rule_expression=rule_string)

    left_child = ASTNode.objects.create(type='operand', value=left_operand)
    right_child = ASTNode.objects.create(type='operand', value=right_operand)

    root.left = left_child
    root.right = right_child
    root.save()
    return root

def evaluate_ast(node, data):
    if node.type == 'operand':
        value = node.value.strip()

        if value in data:  
            return data[value]
        elif value.isdigit():  
            return int(value)
        else:
            return value.strip("'").strip('"')  

    elif node.type == 'operator':
        left_eval = evaluate_ast(node.left, data)
        right_eval = evaluate_ast(node.right, data)

        if node.value in OPERATORS:
            if node.value in ['>', '<', '=']:
                if isinstance(left_eval, int) and isinstance(right_eval, int):
                    return OPERATORS[node.value](left_eval, right_eval)
                elif isinstance(left_eval, str) and isinstance(right_eval, str):
                    if node.value == '=':
                        return OPERATORS['='](left_eval, right_eval)
                    else:
                        return False  
                else:
                    return False  
            elif node.value in ['AND', 'OR']:
                return OPERATORS[node.value](left_eval, right_eval)
    return False

def index(request):
    rule_string = ""
    rule_id = None
    result = None
    error_message = None

    if request.method == 'POST':
        if 'rule_string' in request.POST:
            rule_string = request.POST.get('rule_string')
            try:
                
                if not ASTNode.objects.filter(rule_expression=rule_string).exists():
                    ast_node = create_rule(rule_string)
                    rule_id = ast_node.id
                else:
                    error_message = "Rule already exists."
            except Exception as e:
                error_message = str(e)

        elif 'json_data' in request.POST and 'ast_id' in request.POST:
            json_data = request.POST.get('json_data')
            ast_id = request.POST.get('ast_id')
            try:
                root_node = ASTNode.objects.get(id=ast_id)
                user_data = ast.literal_eval(json_data)
                result = evaluate_ast(root_node, user_data)
            except ASTNode.DoesNotExist:
                error_message = "Rule ID does not exist."
            except Exception as e:
                error_message = str(e)

    return render(request, 'rule_engine/index.html', {
        'rule_string': rule_string,
        'rule_id': rule_id,
        'result': result,
        'error_message': error_message
    })

def view_rules(request):
    rules = ASTNode.objects.filter(type='operator')
    return render(request, 'rule_engine/view_rules.html', {'rules': rules})
