from django.db import models

class Livros(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=15)

class Leitores(models.Model):
    nome = models.CharField(max_length=50,null=False,)
    sobrenome = models.CharField(max_length=50,null=False,)
    cpf = models.CharField(max_length=11)

class Retirada(models.Model):
    id_livro = models.ManyToManyField(Livros)
    id_leitor = models.ForeignKey(Leitores,on_delete=models.CASCADE)
    data_retirada = models.DateField
    data_entrega = models.DateField

