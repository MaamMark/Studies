'''
# Q. 26
money = float(input("Digite o seu salário: R$ "))

if money > 1500:
    print(f"\nCom o reajuste, agora seu salário é R$ {(money * 0.1) + money}")
else:
    print(f"\nCom o reajuste, agora seu salário é R$ {(money * 0.15) + money}")
'''

'''
# Q. 27
number = int(input("Digite o número: "))

if number % 5 == 0 and number % 7 == 0:
    print("\nO número é divisível pelos dois ao mesmo tempo")
else:
    print("\nO número NÃO é divisível pelos dois ao mesmo tempo")
'''

'''
# Q. 28
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a % b == 0:
    print("\nÉ múltiplo")
else:
    print("\nNÃO é múltiplo")
'''

'''
# Q. 29
age = int(input("Qual a sua idade? "))

if age >= 18:
    print("\nVocê é maior de idade")
elif 0 <= age < 18:
    print("\nVocê é menor de idade")
else:
    print("\nIdade inválida >:(")
'''

'''
# Q. 30
money = float(input("Digite o seu salário: R$ "))
ym = money * 12

if ym > 50000:
    print(f"\nCom a taxa de imposto seu salário anual é R$ {ym - (ym * 0.2)}")
else:
    print(f"\nCom a taxa de imposto seu salário anual é R$ {ym - (ym * 0.15)}")
'''

'''
# Q. 31
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))
num = [a, b, c]

if num[0] - num[1] == num[1] - num[2]:
    print("\nFormam uma progressão aritmética")
else:
    print("\nNÃO formam uma progressão aritmética")
'''

'''
# Q. 32
a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))
c = float(input("Digite mais um valor: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        type = "Equilátero"
    if (a == b and b != c) or (a != b and b == c) or (b != a and a == c):
        type = "Isósceles"
    if a != b and b != c:
        type = "Escaleno"
    print(f"\n{type}")
else:
    print("\nEstes segmentos NÃO podem formar um triângulo")
'''

'''
# Q. 33
workH = int(input("Digite a quantidade de horas trabalhadas no mês: "))
workV = float(input("Digite o valor da hora trabalhada: R$ "))

if workH > 160:
    print(f"O seu salário é de R$ {(workV * workH) + (workH * 0.5)}")
else:
    print(f"O seu salário é de R$ {workV * workH}")
'''

'''
# Q. 34
hour = int(input("Qual a hora atual? (utilizar apenas números inteiros - Ex.: 3): "))

if hour >= 6 and hour < 12:
    print("\nBom dia")
elif hour >= 12 and hour < 18:
    print("\nBoa tarde")
elif hour >= 18 and hour < 24:
    print("\nBoa noite")
elif hour >= 0 and hour < 6:
    print("\nBoa madrugada")
else:
    print("Horário inválido.")
'''

'''
# Q. 35
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

if a + b == c and c - a == b:
    print("\nFormam uma sequência de Fibonacci")
else:
    print("\nNÃO formam uma sequência de Fibonacci")
'''

'''
# Q. 36
old = int(input("Digite a sua idade: "))
height = float(input("Digite a sua altura (Ex.: 1.70): "))

if 0 <= old <= 12 and height < 1.50:
    print("\nCriança")
elif 12 < old <= 17:
    print("\nAdolescente")
elif 17 < old <= 59:
    print("\nAdulto")
elif old > 59:
    print("\nIdoso")
else:
    print("\nIdade inválida")
'''

'''
# Q. 37
old = int(input("Digite a sua idade: "))
gender = input("Digite o seu gênero (M - masculino / F - feminino): ").lower()

if 0 <= old <= 12:
    print("\nCriança")
elif 12 < old <= 17:
    print("\nAdolescente")
elif 17 < old <= 59:
    print("\nAdulto")
elif old > 59 and gender == 'f':
    print("\nIdosa")
elif old > 59:
    print("\nIdoso")
else:
    print("\nIdade inválida")
'''

'''
# Q. 38
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a == 0 or b == 0:
    print("\nNão é possível multiplicar por 0")
else:
    if a % b == 0:
        print("\nÉ múltiplo")
    else:
        print("\nNÃO é múltiplo")
'''

'''
# Q. 39
num = int(input("Digite um número: "))
numC = [int(number) for number in str(num)]

if numC[0] == 0 or numC[len(numC) - 1] == 0:
    print("\nNúmero NÃO palíndromo")
else:
    print("\nNúmero é palíndromo")
'''

'''
# Q. 40
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

if a**2 + b**2 == c**2:
    print("Os números formam um triângulo retângulo")
else:
    print("Os números não formam um triângulo retângulo")
'''

'''
# Q. 41
temp = float(input("Digite a temperatura (em °C): "))

if temp < 10:
    print("\nFrio")
elif 10 <= temp < 25:
    print("\nModerado")
elif temp >= 25:
    print("\nQuente")
'''

'''
# Q. 42
old = int(input("Digite a sua idade: "))

if 5 <= old <= 7:
    print("\nInfatil A")
elif 8 <= old <= 10:
    print("\nInfatil B")
elif 11 <= old <= 13:
    print("\nJuvenil A")
elif 14 <= old <= 17:
    print("\nJuvenil B")
elif old >= 18:
    print("\nAdulto")
else:
    print("\nIdade inválida")
'''

'''
# Q. 43
week = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
day = int(input("Digite um número de 1 a 7: "))

if 1 <= day <= 7:
    print(f"\n{week[day - 1]}")
else:
    print("\nPensei ter deixado claro dizer que é um número entre UM e SETE")
'''

'''
# Q. 44
side = int(input("Digite o lado do quadrado: "))

print(f"Área do quadrado: {side * side}")
print(f"Perímetro do quadrado: {side * 4}")
'''

'''
# Q. 45
weight = float(input("Digite o seu peso (Ex.: 60.0): "))
height = float(input("Digite a sua altura (Ex.: 1.70): "))
formula = weight / (height ** 2)

if formula < 18.5:
    print("Abaixo do peso")
elif formula >= 18.5 and formula <= 24.9:
    print("Peso normal")
elif formula >= 25 and formula <= 29.9:
    print("Sobrepeso")
elif formula >= 30 and formula <= 34.9:
    print("Obesidade grau 1")
elif formula >= 35 and formula <= 39.9:
    print("Obesidade grau 2 (severa)")
elif formula >= 40:
    print("Obesidade grau 3 (mórbida)")
'''

'''
# Q. 46
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))
numbers = [a, b, c]

def prime(num):
    if num <= 1:
        return False
    for x in range (2, num):
        if num % x == 0:
            return False
    return True

if prime(a) and prime(b) and prime(c):
    if numbers == sorted(numbers):
        print("\nFormam uma sequência de números primos consecutivos")
    else:
        print("\nNÃO formam uma sequência de números primos consecutivos")
else:
    print("\nUm ou mais números NÃO são primos")
'''

'''
# Q. 47
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
op = input("\nDigite a operação:\n'+' Adição\n'-' Subtração\n'*' Multiplicação\n'/' Divisão\n\nA operação desejada: ")

if op == '+':
    print("\nAdição")
    print(f"O resultado da operação é {a + b}")
elif op == '-':
    print("\nSubtração")
    print(f"O resultado da operação é {a - b}")
elif op == '*':
    print("\nMultiplicação")
    print(f"O resultado da operação é {a * b}")
elif op == '/':
    print("\nDivisão")
    print(f"O resultado da operação é {a / b}")
else:
    print("\nOperação inválida")
'''

'''
# Q. 48
a = int(input("Digite um número inteiro: "))

tim = a ** 2
timStr = str(tim)

half = len(timStr) // 2

lf = int(timStr[:half] or 0)
rg = int(timStr[half:])

if lf + rg == a:
    print(f"{a} é um número de Kaprekar")
else:
    print(f"{a} NÃO é um número de Kaprekar")
'''

'''
# Q. 49
old = int(input("Digite a sua idade: "))

if 0 <= old <= 10:
    print("\nInfatil")
elif 11 <= old <= 17:
    print("\nJuvenil")
elif 18 <= old <= 29:
    print("\nAdulto")
elif 30 <= old <= 50:
    print("\nSênior")
elif old > 50:
    print("\nMáster")
else:
    print("\nIdade inválida")
'''

'''
# Q. 50
a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))
c = float(input("Digite mais um valor: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        type = "Equilátero"
    if (a == b and b != c) or (a != b and b == c) or (b != a and a == c):
        type = "Isósceles"
    if a != b and b != c:
        type = "Escaleno"
    print(f"\nEstes segmentos podem formar um triângulo e o seu tipo é o {type}")
    if a**2 + b**2 == c**2:
        print("Os números formam um triângulo retângulo")
    else:
        print("Os números NÃO formam um triângulo retângulo")
else:
    print("\nEstes segmentos NÃO podem formar um triângulo")
'''