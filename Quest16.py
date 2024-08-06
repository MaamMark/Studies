# QUESTÃO 16 - Peça dois números ao usuário e imprima o resultado da potência do primeiro pelo segundo.

# Variáveis que esperam receber dois valores numéricos (em forma "flutuante" caso queira especificar casas decimais) respectivamente determinados pelo usuário
valueOne = float(input("Insira um número: "))
valueTwo = float(input("Insira outro número: "))
# Escrita no console do resultado da potência do primeiro pelo segundo
print(f"\n{valueOne ** valueTwo}")