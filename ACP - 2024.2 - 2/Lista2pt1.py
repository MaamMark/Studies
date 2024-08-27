'''
# Q. 1
a = input("Digite o valor A: ")
b = input("Digite o valor B: ")
c = input("Digite o valor C: ")
soma = a + b

if (soma) > c:
    print("A soma é maior que o valor C")
elif (soma) < c:
    print("A soma NÃO é maior que o valor C")
'''

'''
# Q. 2
num = float(input("Digite um número: "))

if num > 0:
    print(f"O dobro do seu número POSITIVO é {num * 2}")
if num < 0:
    print(f"O dobro do seu número NEGATIVO é {num * 3}")
'''

'''
# Q. 3
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

if a == b:
    c = a + b
    print(f"A soma dos dois valores é de {c}")
else:
    c = a * b
    print(f"A multiplicação dos dois valores é de {c}")
'''

'''
# Q. 4
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
c = int(input("Digite mais um valor: "))

list = [a, b, c]
list.sort(reverse=True)
'''

'''
# Q. 5
height = float(input("Digite sua altura (Ex.: 1.70): "))
gender = input("Você é homem ou mulher? (M = homem / F = mulher): ").lower()

if gender == 'm':
    print(f"Seu peso ideal é de {round((72.7 * height) - 58, 2)}")
elif gender == 'f':
    print(f"Seu peso ideal é de {round((62.1 * height) - 44.7, 2)}")
else:
    print("Algum erro ocorreu! Verifique se sua digitação está correta.")
'''