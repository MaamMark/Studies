# QUESTÃO 2 - Peça ao usuário para inserir dois números e imprima a soma, a subtração, a multiplicação e a divisão deles.

# Variáveis que esperam receber dois valores (em forma "FLUTUANTE" caso queira especificar casas decimais) respectivamente determinados pelo usuário
valueOne = float(input("Insira um número: "))
valueTwo = float(input("Insira outro número: "))
# Escrita no console de cada operação matemática, sendo soma, subtração, divisão e multiplicação
print(f"A soma dos seus números é: {valueOne + valueTwo}")
print(f"A subtração dos seus números é: {valueOne - valueTwo}")
print(f"A multiplicação dos seus números é: {valueOne * valueTwo}")
print(f"A divisão dos seus números é: {valueOne / valueTwo}")