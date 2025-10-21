from django.contrib import admin

# Importar classes
from .models import Campo, Atividade, Classe, Status, Campus

# Register your models here.
admin.site.register(Campo)
admin.site.register(Atividade)
admin.site.register(Campus)
admin.site.register(Status)
admin.site.register(Classe)