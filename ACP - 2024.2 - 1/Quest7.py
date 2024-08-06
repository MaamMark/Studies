# QUESTÃO 7 - Faça um programa que receba do usuário um valor em metros e forneça o mesmo valor em quilômetros, centímetros e milímetros.

# Variável que espera receber um valor numérico flutuante
value = float(input("Valor em metros a ser convertido: "))
# Escrita no console do valor convertido nas três medidas requisitadas
print(f"\nSeu valor em km: {value / 1000}")
print(f"Seu valor em cm: {value * 100}")
print(f"Seu valor em mm: {value * 1000}")