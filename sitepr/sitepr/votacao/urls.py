from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'votacao'
urlpatterns = [
    path("", views.WebPage, name='WebPage'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logoutview, name="logout"),
    path('registo/', views.registo, name='registo'),
    path('login/votacao/', views.index, name='index'),
    path('login/votacao/profile/<str:username>/', views.profile, name='profile'),
    path('login/votacao/<int:questao_id>/', views.detalhe, name='detalhe'),
    path('login/votacao/<int:questao_id>/resultados/', views.resultados, name='resultados'),
    path('login/votacao/<int:questao_id>/voto/', views.voto, name='voto'),
    path('login/votacao/criarquestao/', views.criarquestao, name="criarquestao"),
    path('login/votacao/<int:questao_id>/apagar_questao/', views.apagar_questao, name="apagar_questao"),
    path('login/votacao/<int:questao_id>/criaropcao/', views.criaropcao, name="criaropcao"),
    path('login/votacao/<int:questao_id>/apagaropcao/<int:opcao_id>/', views.apagar_opcao, name="apagar_opcao"),
]
