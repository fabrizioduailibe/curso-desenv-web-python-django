#from django.shortcuts import render

# Consultar documentação Django para saber o pacote que contem a classe desejada
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividade, Campus, Status, Classe 
from .models import Progressao, Situacao, Comprovante, Validacao, Servidor

# Recursos para ações com o registro após cadastro criado
from django.urls import reverse_lazy

# Recursos para controle de autenticação de usuário
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Importe o widget DateInput
from django.forms import DateInput 

# Para usar telas de erro padrão para objeto não encontrado
from django.shortcuts import get_object_or_404


# Create your views here.


# Criar as classes herdadas de CreateView para criação de cada tipo de cadastro que temos

# Usuários e Administradores podem Criar "Campo". 
# Os demais cadastros somente Administradores podem criar.

class CampoCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Usuarios"]
    model = Campo
    # Informar quais campos deseja que sejam preenchidos -- vide disponíveis em models.py
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    # Em caso de preenchimento correto de todos os campos, vai por enquanto para o início (index)
    success_url = reverse_lazy('listar-campos')

class AtividadeCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

class StatusCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')

class CampusCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campi')

class ClasseCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Docentes"]
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classes')

class SituacaoCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Docentes"]
    model = Situacao
    fields = ['progressao', 'status', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-situacoes')

class ProgressaoCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Docentes", u"Usuarios"]
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressoes')

    # Sobreescreve form_valid para informar o "usuário".
    def form_valid(self, form):       
        # Antes do "super" o objeto não foi criado nem salvo no banco. Para acessar 
        # os campos usa-se a classe "instance" do form.

        # Preenche manualmente o campo "usuário" da instância de dados do form.
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        # Depois do "super" o objeto está criado e salvo. Para acessar os campos
        # usa-se a propriedade "object" da classe ProgressaoCreate.

        # Concatenar " [TESTE]" ao conteúdo de "observacao" e atualizar no banco.
        self.object.observacao += " [TESTE]"
        self.object.save()

        return url

    # 1. Sobrescreva get_form_class para incluir o widget de Calendário para data
    def get_form_class(self):
        """
        Cria dinamicamente uma classe ModelForm com o widget DateInput 
        configurado para o campo 'data'.
        """
        # 2. Obtém a classe ModelForm padrão que o Django usaria.
        form_class = super().get_form_class()
        
        # 3. Cria uma nova classe (subclasse) que herda da classe padrão.
        class ProgressaoFormWithDateInput(form_class):
            class Meta(form_class.Meta):
                # 4. Define o atributo 'widgets' dentro da Meta.
                widgets = {
                    'data_inicial': DateInput(attrs={'type': 'date'},
                        # Força o formato ISO 8601 para a saída HTML.
                        format='%Y-%m-%d'),
                    'data_final': DateInput(attrs={'type': 'date'},
                        # Força o formato ISO 8601 para a saída HTML.
                        format='%Y-%m-%d'),
                }
        # 5. Retorna a nova classe de formulário customizada.
        return ProgressaoFormWithDateInput
    

class ComprovanteCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Docentes", u"Usuarios"]
    model = Comprovante
    fields = ['progressao', 'atividade', 'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comprovantes')

    # 1. Sobrescreva get_form_class para incluir o widget de Calendário para data
    def get_form_class(self):
        """
        Cria dinamicamente uma classe ModelForm com o widget DateInput 
        configurado para o campo 'data'.
        """
        # 2. Obtém a classe ModelForm padrão que o Django usaria.
        form_class = super().get_form_class()
        
        # 3. Cria uma nova classe (subclasse) que herda da classe padrão.
        class ComprovanteFormWithDateInput(form_class):
            class Meta(form_class.Meta):
                # 4. Define o atributo 'widgets' dentro da Meta.
                widgets = {
                    'data': DateInput(attrs={'type': 'date'},
                        # Força o formato ISO 8601 para a saída HTML.
                        format='%Y-%m-%d'),
                    'data_final': DateInput(attrs={'type': 'date'},
                        # Força o formato ISO 8601 para a saída HTML.
                        format='%Y-%m-%d'),
                }
        # 5. Retorna a nova classe de formulário customizada.
        return ComprovanteFormWithDateInput
    

class ValidacaoCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [ u"Administradores", u"Docentes"]
    model = Validacao
    fields = ['comprovante', 'quantidade', 'justificativa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-validacoes')

class ServidorCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Servidor
    fields = ['nome_completo', 'matricula', 'cpf', 'campus']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servidores')



#Editar (UPDATE) as classes herdadas de UpdateView para cada tipo de cadastro que temos

# Usuários e Administradores podem Editar "Campo". 
# Os demais cadastros somente Administradores podem editar

class CampoUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Usuarios"]
    model = Campo
    # Informar quais campos deseja que sejam preenchidos -- vide disponíveis em models.py
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    # Em caso de preenchimento correto de todos os campos, vai por enquanto para o início (index)
    success_url = reverse_lazy('listar-campos')

class AtividadeUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

class StatusUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')

class CampusUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campi')

class ClasseUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Docentes"]
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classes')

class SituacaoUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Docentes"]
    model = Situacao
    fields = ['progressao', 'status', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-situacoes')

class ProgressaoUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Docentes", u"Usuarios"]
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressoes')

    # 1. Sobrescreva get_form_class para incluir o widget de Calendário para data
    def get_form_class(self):
        """
        Cria dinamicamente uma classe ModelForm com o widget DateInput 
        configurado para o campo 'data'.
        """
        # 2. Obtém a classe ModelForm padrão que o Django usaria.
        form_class = super().get_form_class()
        
        # 3. Cria uma nova classe (subclasse) que herda da classe padrão.
        class ProgressaoFormWithDateInput(form_class):
            class Meta(form_class.Meta):
                # 4. Define o atributo 'widgets' dentro da Meta.
                widgets = {
                    'data_inicial': DateInput(attrs={'type': 'date'},
                        # Força o formato ISO 8601 para a saída HTML.
                        format='%Y-%m-%d'),
                    'data_final': DateInput(attrs={'type': 'date'},
                        # Força o formato ISO 8601 para a saída HTML.
                        format='%Y-%m-%d'),
                }
        # 5. Retorna a nova classe de formulário customizada.
        return ProgressaoFormWithDateInput

    # Redefine "get_object" para filtrar não só o padrão (pelo 'pk' do endereço da página), 
    # mas também pelo usuario logado.
    def get_object(self, queryset=None):
        # self.object = Progressao.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        self.object = get_object_or_404(Progressao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class ComprovanteUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Docentes", u"Usuarios"]
    model = Comprovante
    fields = ['progressao', 'atividade', 'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comprovantes')

    # 1. Sobrescreva get_form_class para incluir o widget de Calendário para data
    def get_form_class(self):
        """
        Cria dinamicamente uma classe ModelForm com o widget DateInput 
        configurado para o campo 'data'.
        """
        # 2. Obtém a classe ModelForm padrão que o Django usaria.
        form_class = super().get_form_class()
        
        # 3. Cria uma nova classe (subclasse) que herda da classe padrão.
        class ComprovanteFormWithDateInput(form_class):
            class Meta(form_class.Meta):
                # 4. Define o atributo 'widgets' dentro da Meta.
                widgets = {
                    'data': DateInput(attrs={'type': 'date'},
                        # Força o formato ISO 8601 para a saída HTML.
                        format='%Y-%m-%d'),
                    'data_final': DateInput(attrs={'type': 'date'},
                        # Força o formato ISO 8601 para a saída HTML.
                        format='%Y-%m-%d'),
                }
        # 5. Retorna a nova classe de formulário customizada.
        return ComprovanteFormWithDateInput
    

class ValidacaoUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Docentes"]
    model = Validacao
    fields = ['comprovante', 'quantidade', 'justificativa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-validacoes')

class ServidorUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Servidor
    fields = ['nome_completo', 'matricula', 'cpf', 'campus']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servidores')



# Excluir (DELETE) as classes herdadas de DeleteView para cada tipo de cadastro que temos.

# OBS.: Como não se trata de preencher campos, não é necessário usar o atributo "fields". E usaremos 
# um template específico para exclusão.

# Somente Administradores podem Excluir

class CampoDelete(GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    # Esta propriedade de GroupRequiredMixin gera tela padrão em caso de erros, como
    # acesso de grupo não autorizado. Mas a mensagem é vaga e em inglês. 
    #   raise_exception = True    
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    # Em caso de preenchimento correto de todos os campos, vai por enquanto para o início (index)
    success_url = reverse_lazy('listar-campos')

class AtividadeDelete(GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')

class StatusDelete(GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-status')

class CampusDelete(GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Campus
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campi')

class ClasseDelete(GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-classes')

class SituacaoDelete(GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Situacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-situacoes')

class ProgressaoDelete(GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Progressao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-progressoes')

    # Redefine o método "get_object" herdado de DeleteView. No caso abaixo,
    # está fazendo o padrão que já faz = buscar o registro que tem o campo
    # "pk" do model igual à informação correspondente a "pk" nos argumentos do endereço
    # passado no path, assim como declarados no path que usa o ProgressaoDelete.
    #
    #def get_object(self, queryset=None):
    #    self.object = Progressao.objects.get(pk=self.kwargs['pk'])
    #    return self.object

    # Redefine "get_object" para filtrar não só o padrão (pelo 'pk'), mas também
    # pelo 
    def get_object(self, queryset=None):
        self.object = Progressao.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class ComprovanteDelete(GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Comprovante
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comprovantes')

class ValidacaoDelete(GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administradores"
    model = Validacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-validacoes')



# Listar (LIST) as classes herdadas de DeleteView para cada tipo de cadastro que temos.

# Como se trata apenas de uma página para exibir dados, sem preenchimento, resultado de edição ao
# redirecionamento, só é necessário declarar o "template" nas classes.

# OBS.: Como cada classe tem seus atributos, é necessário indicar um template diferente 
# para cada classe que vai ser listada.

# Como qualquer usuário autenticado pode listar, vamos usar apenas LoginRequiredMixin

class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'

class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'

class StatusList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Status
    template_name = 'cadastros/listas/status.html'

class CampusList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campus
    template_name = 'cadastros/listas/campus.html'

class ClasseList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/listas/classe.html'

class SituacaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Situacao
    template_name = 'cadastros/listas/situacao.html'

class ProgressaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Progressao
    template_name = 'cadastros/listas/progressao.html'

    # Redefine o método de listagem de objetos de ProgressaoList, herdado da classe ListView.
    # Aqui o método está fazendo exatamente o padrão.
    #
    #def get_queryset(self):
    #    self.object_list = Progressao.objects.all()
    #    return self.object_list

    # Redefine o método de listagem de objetos de ProgressaoList para filtrar resultados
    # pelo usuário logado.
    def get_queryset(self):
        self.object_list = Progressao.objects.filter(usuario=self.request.user)
        return self.object_list


class ComprovanteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Comprovante
    template_name = 'cadastros/listas/comprovante.html'

class ValidacaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Validacao
    template_name = 'cadastros/listas/validacao.html'

class ServidorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Servidor
    template_name = 'cadastros/listas/servidor.html'
