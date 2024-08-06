# QUESTÃO 13 - Calcule e imprima a área e o comprimento de uma circunferência. O valor do raio peça ao usuário para digitar.

# Variável que espera um número flutuante
value = float(input("Digite o raio da circunferência: "))
# Escrita no console indicando os valores tanto da circunferência quanto do comprimento (com suas devidadas conversões)
print(f"\nA área dessa circunferência é {2 * 3.14 * value}")
print(f"O comprimento dessa circunferência é {3.14 * (value ** 2)}")