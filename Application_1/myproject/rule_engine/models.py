from django.db import models

class ASTNode(models.Model):
    NODE_TYPES = [
        ('operator', 'Operator'),
        ('operand', 'Operand'),
    ]
    type = models.CharField(max_length=10, choices=NODE_TYPES)
    value = models.CharField(max_length=255, null=True, blank=True)
    left = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='left_child')
    right = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='right_child')
    rule_expression = models.TextField(null=True, blank=True, unique=True)  

    def __str__(self):
        return self.rule_expression if self.rule_expression else f"{self.type}: {self.value}"
