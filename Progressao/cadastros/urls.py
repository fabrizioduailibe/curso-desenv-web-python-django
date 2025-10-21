from django.urls import path
#from .views import IndexView, BasicModelView, AboutView, InitialView

from .views import CampoCreate, AtividadeCreate, ClasseCreate, StatusCreate, CampusCreate
from .views import CampoUpdate, AtividadeUpdate, ClasseUpdate, StatusUpdate, CampusUpdate

urlpatterns = [
    #Estrutura básica
    # path('endereço a partir do diretório base/', minhaview.as_view(), name='nome para a url'),
    #    path('', IndexView.as_view(), name='index'),
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/classe/', ClasseCreate.as_view(), name='cadastrar-classe'),
    path('cadastrar/status/', StatusCreate.as_view(), name='cadastrar-status'),
    path('cadastrar/campus/', CampusCreate.as_view(), name='cadastrar-campus'),

    # Para permitir referenciar diretamente um campo de cadastro no endereço web, usa-se o sub-path
    # "<tipo:nome>", onde tipo = "int", "float", "str" ou "bool". Se for referenciar o ID, que é chave 
    # primária da tabela, o Tango pede nome = "pk", como está abaixo no path abaixo.  
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('editar/classe/<int:pk>/', ClasseUpdate.as_view(), name='editar-classe'),
    path('editar/status/<int:pk>/', StatusUpdate.as_view(), name='editar-status'),
    path('editar/campus/<int:pk>/', CampusUpdate.as_view(), name='editar-campus')
]