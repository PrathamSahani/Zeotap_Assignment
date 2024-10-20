from rest_framework import serializers
from .models import ASTNode

class ASTNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ASTNode
        fields = ['id', 'type', 'value', 'left', 'right']
