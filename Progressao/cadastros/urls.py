from django.urls import path

#from .views import IndexView, BasicModelView, AboutView, InitialView
from .views import CampoCreate, AtividadeCreate, ClasseCreate, StatusCreate, CampusCreate
from .views import ServidorCreate, SituacaoCreate, ValidacaoCreate, ComprovanteCreate, ProgressaoCreate
from .views import CampoUpdate, AtividadeUpdate, ClasseUpdate, StatusUpdate, CampusUpdate
from .views import ServidorUpdate, SituacaoUpdate, ValidacaoUpdate, ComprovanteUpdate, ProgressaoUpdate
from .views import CampoDelete, AtividadeDelete, ClasseDelete, StatusDelete, CampusDelete
from .views import SituacaoDelete, ValidacaoDelete, ComprovanteDelete, ProgressaoDelete
from .views import CampoList, AtividadeList, ClasseList, StatusList, CampusList
from .views import ServidorList, SituacaoList, ValidacaoList, ComprovanteList, ProgressaoList


# Tem que ser "urlpatterns" porque é padrão do Django
urlpatterns = [
    #Estrutura básica
    # path('endereço a partir do diretório base/', minhaview.as_view(), name='nome para a url'),
    #    path('', IndexView.as_view(), name='index'),
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/classe/', ClasseCreate.as_view(), name='cadastrar-classe'),
    path('cadastrar/status/', StatusCreate.as_view(), name='cadastrar-status'),
    path('cadastrar/campus/', CampusCreate.as_view(), name='cadastrar-campus'),
    path('cadastrar/servidor/', ServidorCreate.as_view(), name='cadastrar-servidor'),
    path('cadastrar/situacao/', SituacaoCreate.as_view(), name='cadastrar-situacao'),
    path('cadastrar/validacao/', ValidacaoCreate.as_view(), name='cadastrar-validacao'),
    path('cadastrar/comprovante/', ComprovanteCreate.as_view(), name='cadastrar-comprovante'),
    path('cadastrar/progressao/', ProgressaoCreate.as_view(), name='cadastrar-progressao'),

    # Para permitir referenciar diretamente um campo de cadastro no endereço web, usa-se o sub-path
    # "<tipo:nome>", onde tipo = "int", "float", "str" ou "bool". Se for referenciar o ID, que é chave 
    # primária da tabela, o Tango pede nome = "pk", como está abaixo no path abaixo.  
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('editar/classe/<int:pk>/', ClasseUpdate.as_view(), name='editar-classe'),
    path('editar/status/<int:pk>/', StatusUpdate.as_view(), name='editar-status'),
    path('editar/campus/<int:pk>/', CampusUpdate.as_view(), name='editar-campus'),
    path('editar/servidor/<int:pk>/', ServidorUpdate.as_view(), name='editar-servidor'),
    path('editar/situacao/<int:pk>/', SituacaoUpdate.as_view(), name='editar-situacao'),
    path('editar/validacao/<int:pk>/', ValidacaoUpdate.as_view(), name='editar-validacao'),
    path('editar/comprovante/<int:pk>/', ComprovanteUpdate.as_view(), name='editar-comprovante'),
    path('editar/progressao/<int:pk>/', ProgressaoUpdate.as_view(), name='editar-progressao'),

    # Para permitir referenciar diretamente um campo de cadastro no endereço web, usa-se o sub-path
    # "<tipo:nome>", onde tipo = "int", "float", "str" ou "bool". Se for referenciar o ID, que é chave 
    # primária da tabela, o Tango pede nome = "pk", como está abaixo no path abaixo.  
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),
    path('excluir/classe/<int:pk>/', ClasseDelete.as_view(), name='excluir-classe'),
    path('excluir/status/<int:pk>/', StatusDelete.as_view(), name='excluir-status'),
    path('excluir/campus/<int:pk>/', CampusDelete.as_view(), name='excluir-campus'),
    path('excluir/situacao/<int:pk>/', SituacaoDelete.as_view(), name='excluir-situacao'),
    path('excluir/validacao/<int:pk>/', ValidacaoDelete.as_view(), name='excluir-validacao'),
    path('excluir/comprovante/<int:pk>/', ComprovanteDelete.as_view(), name='excluir-comprovante'),
    path('excluir/progressao/<int:pk>/', ProgressaoDelete.as_view(), name='excluir-progressao'),

    # Listar
    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/atividades/', AtividadeList.as_view(), name='listar-atividades'),
    path('listar/classes/', ClasseList.as_view(), name='listar-classes'),
    path('listar/campi/', CampusList.as_view(), name='listar-campi'),
    path('listar/status/', StatusList.as_view(), name='listar-status'),
    path('listar/servidores/', ServidorList.as_view(), name='listar-servidores'),
    path('listar/situacoes/', SituacaoList.as_view(), name='listar-situacoes'),
    path('listar/validacoes/', ValidacaoList.as_view(), name='listar-validacoes'),
    path('listar/comprovantes/', ComprovanteList.as_view(), name='listar-comprovantes'),
    path('listar/progressoes/', ProgressaoList.as_view(), name='listar-progressoes'),

]