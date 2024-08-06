# QUESTÃO 12 - Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a.m.

# Variável que espera receber um número flutuante
value = float(input("Digite o valor do depósito: "))
# Escrita no console indicando qual será o valor após o incremento da taxa de 0,7%
print(f"\nO valor que renderá após um mês é de R$ {(value * 0.007) + value}")