from django.db import models
from .validators import validate_matricula
from localflavor.br.models import BRCPFField
from django.contrib.auth.models import User



# Métodos e Choices

def user_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "uploads/usuario_{0}/{1}".format(instance.user.id, filename)



# Create your models here.

class Campo(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    # Função padrão. Aqui defino o que eu quero que seja feito quando um objeto 
    # deste tipo for impresso.
    def __str__(self):
    #    return super().__str__()

        # Formatação de string de saída
        return "{} ({})".format(self.nome, self.descricao)

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número", unique=True)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    # pontos = models.FloatField()
    pontos = models.DecimalField(max_digits=5, decimal_places=2)
    detalhes = models.CharField(max_length=100, blank=True, null=True, default="NSA")
    # Atividade tem relação N:1 com Campo. Campo é uma chave estrangeira para Atividade
    # PROTECT impede que o Campo seja deletado se já houver alguma Atividade vinculada a ele.
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__(self):
        # Formatação de string de saída
        return "{} ({}) - {}".format(self.numero, self. descricao, self.campo)

class Status(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome", unique=True)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)
    
class Classe(models.Model):
    nome = models.CharField(max_length=50)
    nivel = models.IntegerField(verbose_name="Nível")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    class Meta:
        # Define que a combinação de 'cidade' e 'endereco'
        # DEVE ser única em toda a tabela.
        unique_together = [['nome', 'nivel'],]

    def __str__(self):
        return "{} | Nível {}".format(self.nome, self.nivel)
    
class Campus(models.Model):
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150, verbose_name="Endereço")
    telefone = models.CharField(max_length=15)

    class Meta:
        # Define que a combinação de 'cidade' e 'endereco'
        # DEVE ser única em toda a tabela.
        unique_together = [['cidade', 'endereco'],]

    def __str__(self):
        return "{} | {}".format(self.cidade, self.endereco)
    
class Progressao(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT, verbose_name="Classe pretendida")
    data_inicial = models.DateField(verbose_name="Data inicial")
    data_final = models.DateField(verbose_name="Data final")
    observacao = models.CharField(max_length=150, verbose_name="Observação")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")

    def __str__(self):
        return "{} -> {} | {} a {}".format(self.usuario, self.classe, self.data_inicial, 
            self.data_final)
 
class Situacao(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    detalhes = models.CharField(max_length=150)
    progressao = models.ForeignKey(Progressao, on_delete=models.PROTECT)
    # "auto_now" força o campo a se preencher automaticamente com a datetime do momento 
    # da criação ou modificação.
    movimentado_em = models.DateTimeField(auto_now=True, verbose_name="Movimentado em")
    movimentado_por = models.ForeignKey(User, on_delete=models.PROTECT, 
        verbose_name="Movimentado por")

    def __str__(self):
        return "[{}] {} - {} / {} | {} - {}".format(self.pk, self.status, 
            self.detalhes, self.progressao, self.movimentado_em, self.movimentado_por)

class Comprovante(models.Model):
    progressao = models.ForeignKey(Progressao, on_delete=models.PROTECT, verbose_name="Progressão")
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2, max_digits=5)
    data = models.DateField()
    data_final = models.DateField(null=True, blank=True, help_text="Informar apenas se o comprovante" \
        "for relativo a um período", verbose_name="Data final")
    ultima_modificacao = models.DateTimeField(auto_now=True, verbose_name="Última modificação")
    arquivo = models.FileField(upload_to=user_path)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")

    def __str__(self):
        return "[{}] {} / {} - {} - {} a {} - {}".format(self.pk, self.atividade, self.progressao,
            self.quantidade, self.data, self.data_final, self.usuario)

class Validacao(models.Model):
    comprovante = models.ForeignKey(Comprovante, on_delete=models.PROTECT)
    # "auto_now_add" força o campo a se preencher automaticamente com a datetime do momento 
    # da criação.
    validado_em = models.DateTimeField(auto_now_add=True, verbose_name="Validade em")
    validado_por = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Validade por")
    quantidade = models.DecimalField(max_digits=5, decimal_places=2)
    justificativa = models.CharField(max_length=255)

    def __str__(self):
        return "[{}] Pontuação: {}/{} - {}".format(self.comprovante.pk, self.quantidade, 
            self.comprovante.quantidade, self.validado_por)

class Servidor(models.Model):
    nome_completo = models.CharField(max_length=50, verbose_name="Nome completo")
    matricula = models.CharField(
        max_length=7,
        verbose_name="Matrícula",
        unique=True,
        validators=[validate_matricula], # Aplica o validador
        help_text="Formato esperado: XX-NNNN (ex: AB-1234)"
    )
    cpf = BRCPFField("CPF", unique=True) # Este campo já valida o formato e o dígito verificador
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {} - {} / {}".format(self.nome_completo, 
            self.matricula, self.cpf, self.campus)
    
    def get_cpf_mascarado(self):
        """
        Retorna o CPF no formato: ******856-**
        Assume que o CPF tem 11 dígitos (apenas números).
        """
        if self.cpf and len(self.cpf) == 11:
            # Pegamos os primeiros 6 dígitos e substituímos por asteriscos
            inicio = "******"
            # Pegamos os penúltimos 3 dígitos
            fim_parte1 = self.cpf[6:9] 
            # Pegamos os últimos 2 dígitos (dígitos verificadores) e substituímos por asteriscos
            fim_parte2 = "**"

            return f"{inicio}{fim_parte1}-{fim_parte2}"
        
        # Retorna "0" se não for um CPF válido de 11 dígitos
        return 0

