from django.db.models import *

from votacao.models import Questao, Opcao

purp = "\033[35m"
nocolor = "\033[0m"
blue = "\033[45m"
cyan = "\033[34m"
underline = "\033[4m"

print("\n#########################################")

# pergunta 1

print(f"{underline}{purp}Número total de votos na base de dados{nocolor}:{blue}",
      Questao.objects.aggregate(Sum('opcao__votos'))['opcao__votos__sum'],
      f"{nocolor}votos"
      )

print(f"Questões:{blue}", Questao.objects.count(),
      f"{nocolor}Opções: {blue}", Opcao.objects.count(), f"{nocolor}")

# pergunta 2
print("#########################################\n")
for questao in Questao.objects.all():
    opcao_mais_votada = questao.opcao_set.annotate(max_votos=Max('votos')).order_by('-max_votos').first()
    if opcao_mais_votada:
        print(f"Questão:\"{cyan}", questao.questao_texto, f"{nocolor}\"--->  Mais votada <{blue}",
              opcao_mais_votada.opcao_texto,
              f"{nocolor}>")
    else:
        print("Nenhuma opção encontrada para esta questão.")
