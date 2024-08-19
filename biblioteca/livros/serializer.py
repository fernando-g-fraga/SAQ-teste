from rest_framework import serializers
from livros.models import Livros,Retirada,Leitores


class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = ['id','title','author','serial_number']

class RetiradaSerializer(serializers.ModelSerializer):
    # livros = LivrosSerializer(many=True,read_only=True)

    class Meta:
        model = Retirada
        fields = ['id','data_retirada', 'data_entrega'] 

class LeitoresSerializer(serializers.ModelSerializer):    
    # leitores = RetiradaSerializer(many=True,read_only=True)
    class Meta:
        model = Leitores
        fields = ['id','nome','sobrenome','cpf']

