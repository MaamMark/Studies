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

'''
# Q. 6
weight = float(input("Digite o seu peso (Ex.: 60.0): "))
height = float(input("Digite a sua altura (Ex.: 1.70): "))
formula = weight / (height ** 2)

if formula < 18.5:
    print("Você está abaixo do peso")
elif formula >= 18.5 and formula < 25:
    print("Você está com peso normal")
elif formula >= 25 and formula < 30:
    print("Você está acima do peso")
elif formula >= 30:
    print("Você está obeso")
'''

'''
# Q. 7
value = float(input("Valor da etiqueta: R$ "))
option = int(input("\nSelecione a opção de pagamento:\n 1. À vista em dinheiro ou cheque\n 2. À vista no cartão de crédito\n 3. Parcelado em duas vezes\n 4. Parcelado em três vezes\nDetermine sua escolha (Ex.: 1): "))

def price (option, value):
    if option == 1:
        value -= (value * 0.1)
    elif option == 2:
        value -= (value * 0.15)
    elif option == 3:
        value = value
    elif option == 4:
        value += (value * 0.10)
    print(f"O valor final do seu produto é de R$ {value}")

price(option, value)
'''

'''
# Q. 8
gradeOne = float(input("Indique sua primeira nota: "))
gradeTwo = float(input("Indique sua segunda nota: "))
gradeThree = float(input("Indique sua terceira nota: "))
ma = (gradeOne + gradeTwo * 2 + gradeThree * 3 + ((gradeOne + gradeTwo + gradeThree) / 3)) / 7

if ma >= 9.0:
    print("Conceito final: A")
elif ma >= 7.5 and ma < 9.0:
    print("Conceito final: B")
elif ma >= 6.0 and ma < 7.5:
    print("Conceito final: C")
elif ma >= 4.0 and ma < 6.0:
    print("Conceito final: D")
elif ma < 4.0:
    print("Conceito final: F")
'''

'''
# Q. 9 e Q. 10
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
else:
    print("\nEstes segmentos NÃO podem formar um triângulo")
'''

'''
# Q. 11
a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))
c = float(input("Digite mais um valor: "))

list = [a, b, c]
list.sort(reverse=True)

print(list[0])
'''

'''
# Q. 12
shift = input("Indique o turno de estudo (M - matutino / V - vespertino / N - noturno): ").lower()

if shift == 'm':
    print("Bom Dia!")
elif shift == 'v':
    print("Bom Tarde!")
elif shift == 'n':
    print("Boa Noite!")
else:
    print("Você digitou incorretamente...")
'''

'''
# Q. 13
grades = [200, 100, 50, 10, 5, 2]
gradeNum = {}

value = int(input("Digite o valor do saque (mín. R$ 20 / máx. R$ 500): "))

if value <= 500 and value >= 20:
    for nota in grades:
        gradeNum[nota] = value // nota
        value %= nota

    print("Quantidade de notas fornecidas:")

    for nota, quantidade in gradeNum.items():
        if quantidade > 0:
            print(f"Notas de R${nota}: {quantidade}")
    
else:
    print("\nVocê ultrapassou os limites estipulados")
'''

'''
# Q. 14
questOne = input("Sobre o crime, você telefonou para a vítima? (Y - sim/ N - não): ").lower()
questTwo = input("Mora perto da vítima? (Y - sim/ N - não): ").lower()
questThree = input("Devia para a vítima? (Y - sim/ N - não): ").lower()
questFour = input("Já trabalhou com a vítima? (Y - sim/ N - não): ").lower()
questFive = input("Esteve no local do crime? (Y - sim/ N - não): ").lower()
answers = [questOne, questTwo, questThree, questFour, questFive]

if answers.count('y') == 2:
    print("\nSuspeita")
elif answers.count('y') >= 3 and answers.count('y') <= 4:
    print("\nCúmplice")
elif answers.count('y') == 5:
    print("\nAssasino")
else:
    print("\nInocente")
'''

'''
# Q. 15
print("\t\tAté 5Kg\t\tAcima de 5Kg\n1. Filé duplo\tR$ 4,90 o Kg\tR$ 5,80 o Kg\n2. Alcatara\tR$ 5,90 o Kg\tR$ 6,80 o Kg\n3. Picanha\tR$ 6,90 o Kg\tR$ 7,80 o Kg")

type = int(input("\nDigite o tipo de carne que você deseja (Ex.: 1 para Filé duplo): ")) - 1
kg = float(input("Digite a quantidade de carne em Kg (Ex.: 1.5): "))
payment = int(input("\nMétodos de pagamento:\n1. Cartão Altamirão\n2. Cartão de crédito\n3. Pix\n4. Cédula\n\nO método de pagamento será (Ex.: 1 para Cartão Altamirão): ")) - 1

meatList = ["Filé duplo", "Alcatara", "Picanha"]
meatPrice = [4.90, 5.90, 6.90]
paymentList = ["Cartão Altamirão", "Cartão de crédito", "Pix", "Cédula"]

if type <= 2 and type >= 0 and payment <= 3 and payment >= 0:
    if kg <= 5:
        price = meatPrice[type] * kg
    elif kg > 5:
        price = (meatPrice[type] + 0.90) * kg
    
    if payment != 0:
        print(f"\nAgradecemos por confiar no nosso trabalho! Abaixo se encontra o cupom fiscal da compra :D\n\nTipo de carne: {meatList[type]}\nQuantidade: {kg} Kg\nPreço total: R${price}\nMétodo de pagamento: {paymentList[payment]}\nValor do desconto: R$ {0}\nTotal a pagar: R$ {price}\n")
    else:
        print(f"\nAgradecemos por confiar no nosso trabalho! Abaixo se encontra o cupom fiscal da compra :D\n\nTipo de carne: {meatList[type]}\nQuantidade: {kg} Kg\nPreço total: R$ {price}\nMétodo de pagamento: {paymentList[payment]}\nValor do desconto: R$ {round(price * 0.05, 2)}\nTotal a pagar: R$ {(price * 0.05) + price}\n")
else:
    print("\nAlgum dos valores especificados está fora dos limites, verifique se você digitou corretamente :(\n")
'''

'''
# Q. 16
type = int(input("Tipo de temperatura que será convertido:\n1. Celsius\n2. Fahrenheit\n3. Kelvin\n\nSelecione uma opção (Ex.: 1 para Celsius): "))
temp = float(input("Digite o valor da temperatura: "))

if type == 1:
    print(f"\nO valor convertido para Fahrenheit é de {round((temp * 9/5) + 32, 1)}, enquanto para Kelvin é de {round(temp + 273.15, 1)}")
elif type == 2:
    print(f"\nO valor convertido para Celsius é de {round((temp - 32) * 5/9, 1)}, enquanto para Kelvin é de {round((temp - 32) * 5/9 + 273.15, 1)}")
elif type == 3:
    print(f"\nO valor convertido para Celsius é de {round(temp - 273.15, 1)}, enquanto para Fahrenheit é de {round((temp - 273.15) * 9/5 + 32, 1)}")
else:
    print("\nValor fora dos limites estabelecidos")
'''

'''
# Q. 17
capacity = float(input("Qual a capacidade máxima do elevador? (Em Kg - Ex.: 500): "))
peopleW = 0

for x in range (0, 5):
    people = float(input(f"Qual o peso da pessoa {x + 1}? (Em Kg - Ex.: 60.0): "))
    peopleW += people

if peopleW > capacity:
    print("\nO elevador excedeu a carga máxima.")
else:
    print("\nO elevador está liberado para subir")
'''

'''
# Q. 18
a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))
c = float(input("Digite mais um valor: "))
d = float(input("Digite mais outro valor: "))

if b > c and d > a and (c + d) > (a + b) and c >= 0 and d >= 0 and a % 2 == 0:
    print("\nValores aceitos")
else:
    print("\nValores NÃO aceitos")
'''

'''
# Q. 19
year = int(input("Digite o ano: "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("\nAno bissexto")
else:
    print("\nAno NÃO bissexto")
'''

'''
# Q. 20
name = input("Digite o seu nome: ")
dAmount = int(input("Digite a quantidade de dias da semana cursando: "))
cType = input("Digite o nível do seu curso (B - básico / I - intermediário / A - avançado): ").lower()

if cType == 'b':
    print(f"\nNome: {name}\nValor a ser pago: R$ {(dAmount * 7) * 15}")
elif cType == 'i':
    print(f"\nNome: {name}\nValor a ser pago: R$ {(dAmount * 8.5) * 20}")
elif cType == 'a':
    print(f"\nNome: {name}\nValor a ser pago: R$ {(dAmount * 10) * 25}")
else:
    print("Valor inválido")
'''

'''
# Q. 21
distance = float(input("Digite a distância percorrida em quilômetros: "))
time = float(input("Digite o tempo gasto em horas: "))

v = distance / time

if v < 100:
    print("Carro devagar")
elif v >= 100 and v <= 140:
    print("Carro com velocidade mediana")
elif v > 140:
    print("Carro com alta velocidade")

print(f"Velocidade média: {round(v, 2)} km/h")
'''

'''
# Q. 22
l1 = float(input("Digite a nota da L1: "))
l2 = float(input("Digite a nota da L2: "))
p1 = float(input("Digite a nota da P1: "))
l3 = float(input("Digite a nota da L3: "))
l4 = float(input("Digite a nota da L4: "))
p2 = float(input("Digite a nota da P2: "))
l5 = float(input("Digite a nota da L5: "))
p3 = float(input("Digite a nota da P3: "))
l6 = float(input("Digite a nota da L6: "))
l7 = float(input("Digite a nota da L7: "))

m = (((l1 + l2) / 2) + ((p1 + l3 + l4) / 3) + ((p2 + l5) / 2) + ((p3 + l6 + l7) / 3)) / 4

if m < 4:
    print("\nReprovado")
elif m >= 4 and m < 7:
    print("\nRecuperação")
elif m > 7:
    print("\nAprovado")
'''
    
'''
# Q. 23
money = float(input("Digite o valor do salário bruto do colaborador: R$ "))
rMoney = money - (money * 0.15) - (money * 0.10)

if rMoney < 1000:
    print("\nColaborador receberá cesta básica e gratificação")
elif 1000 <= rMoney <= 2000:
    print("\nColaborador receberá apenas gratificação")
elif rMoney > 2000:
    print("\nColaborador receberá apenas a metade da gratificação")

print(f"Salário líquido: R$ {round(rMoney, 2)}")
'''

'''
# Q. 24
meter = float(input("Valor em metros: "))
type = int(input("Tipo de comprimento que será convertido:\n1. Quilômetro\n2. Centímetro\n3. Milímetro\n\nSelecione uma opção (Ex.: 1 para Quilômetro): "))

if type == 1:
    print(f"\nO valor convertido para Quilômetro é de {meter / 1000}")
elif type == 2:
    print(f"\nO valor convertido para Centímetro é de {meter * 100}")
elif type == 3:
    print(f"\nO valor convertido para Milímetro é de {meter * 1000}")
else:
    print("\nErro no sistema")
'''

'''
# Q. 25
import time as tm
import random as rn

print("\nUm programa que busca decidir por você caso esteja indeciso!")
tm.sleep(0.5)
print("\nSe você abriu, quer uma resposta de SIM ou NÃO")
tm.sleep(1)
print("\nCarregando...")
tm.sleep(2)

answer = rn.randint(0, 1)

if answer == 0:
    print("\nA resposta é SIM meu amigo :D")
elif answer == 1:
    print("\nA resposta é NÃO meu amigo :D")
'''