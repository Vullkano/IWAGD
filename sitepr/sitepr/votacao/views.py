from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Questao, Opcao, Aluno
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test


def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'votacao/index.html', context)


def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})


def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/resultados.html', {'questao': questao})


"""
@login_required(login_url=login)
def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        # Apresenta de novo o form para votar
        return render(request, 'votacao/detalhe.html', {'questao': questao,
                                                        'error_message': "Não escolheu uma opção", })
    else:
        opcao_seleccionada.votos += 1
        opcao_seleccionada.save()
        # Retorne sempre HttpResponseRedirect depois de
        # tratar os dados POST de um form
        # pois isso impede os dados de serem tratados
        # repetidamente se o utilizador
        # voltar para a página web anterior.
    return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))
"""


@login_required(login_url=login)
def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    aluno = Aluno.objects.get(user=request.user)

    # Verifica se o número máximo de votos é maior que zero
    if aluno.max_votos > 0:
        try:
            opcao_selecionada = questao.opcao_set.get(pk=request.POST['opcao'])
        except (KeyError, Opcao.DoesNotExist):
            return render(request, 'votacao/detalhe.html', {
                'questao': questao,
                'error_message': "Não escolheu uma opção",
            })
        else:
            opcao_selecionada.votos += 1
            opcao_selecionada.save()

            # Diminui o número máximo de votos em 1
           # aluno.max_votos -= 1
            aluno.votar()
            aluno.save()
    else:
        # Se o número máximo de votos for zero ou menor, mostra uma mensagem de erro
        return render(request, 'votacao/detalhe.html', {
            'questao': questao,
            'error_message': "Limite de votos atingido",
        })

    return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))



@user_passes_test(lambda user: user.is_superuser, login_url=login)
def criarquestao(request):
    if request.method == 'POST':
        novo_texto_questao = request.POST['nova_questao']
        nova_questao = Questao(questao_texto=novo_texto_questao, pub_data=timezone.now())
        nova_questao.save()

        return redirect('votacao:index')
    return render(request, 'votacao/criarquestao.html')


@user_passes_test(lambda user: user.is_superuser, login_url=login)
def apagar_questao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    questao.delete()
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    return render(request, 'votacao/index.html', {'latest_question_list': latest_question_list})


@user_passes_test(lambda user: user.is_superuser, login_url=login)
def criaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    if request.method == 'POST':
        novo_texto_opcao = request.POST['nova_opcao']
        nova_opcao = Opcao(questao=questao, opcao_texto=novo_texto_opcao, votos=0)
        nova_opcao.save()

        # Obtém a URL da página da questão usando reverse
        questao_url = reverse('votacao:detalhe', args=[questao.id])

        # Redireciona para a página da questão
        return redirect(questao_url)

    return render(request, 'votacao/criaropcao.html', {'questao': questao})


@user_passes_test(lambda user: user.is_superuser, login_url=login)
def apagar_opcao(request, questao_id, opcao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    opcao = get_object_or_404(Opcao, pk=opcao_id)
    opcao.delete()
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))


def pagina_nao_encontrada(request, exception):
    return render(request, 'votacao/404.html', status=404)


def pagina_sucesso(request):
    return render(request, 'votacao/info_pessoal.html')


def login_view(request):
    if request.method == 'POST':
        # Verificar o reCAPTCHA
        recaptcha_response = request.POST.get('g-recaptcha-response')
        if recaptcha_response:
            # TODO: Verifique a reCAPTCHA com o Google usando recaptcha_response

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('votacao:index'))
            else:
                error_message = 'Dados introduzidos incorretos. Tente novamente.'
                return render(request, 'votacao/login.html', {'error_message': error_message})
        else:
            error_message = 'Por favor, prove que você não é um robô.'
            return render(request, 'votacao/login.html', {'error_message': error_message})
    else:
        return render(request, 'votacao/login.html')


@login_required(login_url=login)
def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'votacao/login.html')
    # direccionar para página de sucesso
    return render(request, 'votacao/login.html')


def registo(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        curso = request.POST['curso']
        numero_grupo = request.POST['numero_grupo']

        # Definindo user como None inicialmente
        user = None

        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe")
            return render(request, 'votacao/registo.html')

        # Cria o usuário
        user = User.objects.create_user(username, email, password)

        # Se user não for None, então salve-o
        if user is not None:
            user.save()

        # Cria o objeto Aluno para todos os usuários registrados
        aluno = Aluno(user=user, curso=curso, numero_grupo=numero_grupo, max_votos=int(numero_grupo) + 10)
        aluno.save()

        # Redireciona para a página de login após o registro bem-sucedido
        return redirect('votacao:login')

    else:
        return render(request, 'votacao/registo.html')



@login_required(login_url=login_view)
def profile(request, username):
    usr = get_object_or_404(User, username=username)
    return render(request, 'votacao/info_pessoal.html', {
        'usr': usr,
    })

# @login_required(login_url=login_view)
# def info_pessoal(request, username):
#     if request.user.is_authenticated:
#         user = get_object_or_404(User, username=username)
#         return render(request, 'votacao/info_pessoal.html', {
#             'usr': user,
#         })
#     else:
#         return HttpResponseRedirect(reverse('votacao:index'))

def WebPage(request):
    return render(request, 'votacao/WebPage.html')

