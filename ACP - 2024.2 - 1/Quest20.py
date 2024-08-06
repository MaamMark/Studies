# QUESTÃO 20 - Peça ao usuário que insira uma palavra e imprima a mesma palavra repetida três vezes, sem usar repetições ou estruturas de dados.

# Variável que espera receber qualquer valor
value = input("Digite uma palavra: ")
# Laço de repetição que faz um loop de três ciclos, repetindo a mesma palavra 3 vezes
for x in range(0, 3):
    # Condicional criada para que no primeiro ciclo ele dê um espaço do input (o "\n")
    if x == 0:
        print(f"\n{value}")
    else:
        print(f"{value}")