from django.urls import path

# Importando bibliotecas de autenticação, com outro nome diferente de "views", para não 
# confundir com o "views" já existente no módulo. 
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Como LoginView é uma view já pronta, não podemos declarar propriedades dela. Então elas devem
    # ser passadas como parâmetro na chamada.
    path('login/', auth_views.LoginView.as_view(template_name = "usuarios/login.html"), name="login"),
    # Logout não precisa passar parâmetros.
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]