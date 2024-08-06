# QUESTÃO 17 - Peça ao usuário para inserir dois números e imprima o resultado da divisão inteira do primeiro pelo segundo.

# Variáveis que esperam receber dois valores numéricos (em forma "flutuante" caso queira especificar casas decimais) respectivamente determinados pelo usuário
valueOne = float(input("Insira um número: "))
valueTwo = float(input("Insira outro número: "))
# Escrita no console do resultado da divisão inteira do primeiro pelo segundo.
print(f"\n{valueOne // valueTwo}")