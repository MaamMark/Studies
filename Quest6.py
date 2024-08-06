# QUESTÃO 6 - Faça um programa que usuário entre com o valor de um salário de um colaborador e que o programa apresente o salário desse colaborador depois de descontado 15% de imposto e 10% de INSS (aposentadoria).

# Variável que espera receber um número indicando o valor do salário
money = float(input("Digite o valor do salário: R$ "))
# Escrita no console que indica o total do salário final já descontado
print(f"\nSeu salário final é {money - ((money * 0.15) + (money * 0.10))}")