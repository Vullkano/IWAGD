from votacao.models import Questao, Opcao
from django.db.models import Sum, Max

total_de_votos = Questao.objects.aggregate(Sum('opcao__votos'))['opcao__votos__sum']
print(total_de_votos)




questoes = Questao.objects.all()


for questao in questoes:

    opcao_mais_votada = questao.opcao_set.annotate(max_votos=Max('votos')).order_by('-max_votos').first()


    print("Texto da Questão:", questao.questao_texto)


    if opcao_mais_votada:
        print("Texto da Opção Mais Votada:", opcao_mais_votada.opcao_texto)
    else:
        print("Nenhuma opção encontrada para esta questão.")

    print("\n")







