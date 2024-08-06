# QUESTÃO 8 - Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final (depois das comissões) do mês.

# Variáveis que esperam receber respectivamente: qualquer valor (nome pode ser qualquer coisa) e dois números flutuantes em sequência
name = input("Digite o seu nome: ")
money = float(input("Digite o valor do seu salário: "))
sell = float(input("Digite quanto suas vendas renderam: "))
# Escrita no console dos dados requisitados na questão, além da conversão do salário final do vendedor
print(f"\nNome: {name}")
print(f"Salário fixo: {money}")
print(f"Salário final: {(sell * 0.15) + money}")