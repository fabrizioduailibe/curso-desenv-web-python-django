import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_matricula(value):
    """
    Validador customizado para o formato 'XX-NNNN'.
    XX = Caracteres alfabéticos (letras de A-Z)
    NNNN = Dígitos numéricos (0-9)
    """
    # Expressão Regular para o formato:
    # ^      -> Início da string
    # [A-Za-z]{2} -> Exatamente 2 letras (maiúsculas ou minúsculas)
    # -      -> Um hífen literal
    # [0-9]{4} -> Exatamente 4 dígitos numéricos
    # $      -> Fim da string
    pattern = r'^[A-Za-z]{2}-[0-9]{4}$'

    if not re.match(pattern, value):
        raise ValidationError(
            # Mensagem de erro que será exibida para o usuário
            _('%(value)s não está no formato correto. Use o formato XX-NNNN (ex: AB-1234).'),
            params={'value': value},
            code='formato_invalido'
        )