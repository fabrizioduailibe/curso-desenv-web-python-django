from django.db import models

# Create your models here.

class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    # Função padrão. Aqui defino o que eu quero que seja feito quando um objeto 
    # deste tipo for impresso.
    def __str__(self):
    #    return super().__str__()

        # Formatação de string de saída
        return "{} ({})".format(self.nome, self.descricao)

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    # pontos = models.FloatField()
    pontos = models.DecimalField(max_digits=5, decimal_places=1)
    detalhes = models.CharField(max_length=100)

    # Atividade tem relação N:1 com Campo. Campo é uma chave estrangeira para Atividade
    # PROTECT impede que o Campo seja deletado se já houver alguma Atividade vinculada a ele.
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__(self):
        # Formatação de string de saída
        return "{} ({}) - {}".format(self.numero, self. descricao, self.campo)

class Status(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)
    
class Classe(models.Model):
    nome = models.CharField(max_length=50)
    nivel = models.IntegerField(verbose_name="Nível")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
        return "{} ({}) - {}".format(self.nome, self.descricao, self.nivel)
    
class Campus(models.Model):
    cidade = models.CharField(max_length=30)
    endereco = models.CharField(max_length=70, verbose_name="Endereço")
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return "{} - {} / {}".format(self.cidade, self.endereco, self.telefone)
    