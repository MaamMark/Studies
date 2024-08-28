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

# Q. 35
