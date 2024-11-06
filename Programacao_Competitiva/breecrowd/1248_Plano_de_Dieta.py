"""
# ENTENDENDO O PROBLEMA

SE TEM UMA LISTA DE ALIMENTOS QUE VOCÊ DEVE COMER AO LONGO DO DIA (CHAMADA DE DIETA). DEPOIS, VOCE RECEBE DUAS LISTAS
DE ALIMENTOS QUE VOCE JA COMEU NO CAFE DA MANHA E NO ALMOCO.

O OBJETIVO É DESCOBRIR O QUE RESTA NA LISTA DE DIETA PARA COMER NO JANTAR. MAS TEM UM PORÉM: SE VOCE JA COMEU ALGO A MAIS
(ALGO QUE NAO ESTAVA NA DIETA) OU COMEU UM ALIMENTO MAIS VEZES DO QUE O PERMITIDO, VOCE É CONSIDERADO "TRAPACEIRO".

RESUMO:
    * Verificar se você comeu algum alimento que não estava na dieta. Se sim, você "trapaceou".
    * Verificar se você comeu algum alimento mais vezes do que ele aparece na dieta. Se sim, você "trapaceou".
    * Se você não "trapaceou", mostre o que sobrou para o jantar, ordenado em ordem alfabética.
"""

# numero de casos de testes
n = int(input().strip()) # quantidade de casos de teste

# resolvendo cada caso tese
for _ in range(n):
    # dieta, cafe da manha e almoco
    dieta = input().strip() # Lista de alimentos da dieta
    cafe_da_manha = input().strip() # Alimentos do cafe da manha
    almoco = input().strip()

    dieta_set = set(dieta) # alimentos permitidos pela dieta
    comida_consumida = set(cafe_da_manha + almoco) # alimentos consumidos

    # verificar se todos os alimentos ingeridos fazem parte da dieta
    # se alguma comida consumida nao esta na dieta, a pessoa trapaceou
    if not comida_consumida.issubset(dieta_set):
        print("CHEATER")
    else:
        # alimentos da dieta que ainda não foram consumidos
        jantar = sorted(dieta_set - comida_consumida)  # alimentos restantes em ordem alfabética
        print("".join(jantar))

