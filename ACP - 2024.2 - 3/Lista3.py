# FOR
'''
# Q. 1
numero = int(input("Digite um número: "))
soma = 0
for i in range(1, numero + 1):
    soma += i
print(f"A soma de 1 até {numero} é {soma}.")
'''

'''
# Q. 2
for i in range(1, 51):
    print(i)
'''

'''
# Q. 3
for i in range(1, 81):
    if i % 2 == 0:
        print(i)
'''

'''
# Q. 4
for i in range(5, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
'''

'''
# Q. 5
texto = input("Digite uma string: ")
texto_invertido = ""
for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]
print(texto_invertido)
'''

'''
# Q. 6
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Pode trocar pelos números desejados
pares = 0
impares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
'''

'''
# Q. 7
numero = int(input("Digite um número: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero} é {fatorial}.")
'''

'''
# Q. 8
dentro_intervalo = 0
fora_intervalo = 0
for i in range(10):
    numero = int(input("Digite um número: "))
    if 10 <= numero <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1
print(f"Números no intervalo [10, 20]: {dentro_intervalo}")
print(f"Números fora do intervalo: {fora_intervalo}")
'''

'''
# Q. 9
candidato1 = 0
candidato2 = 0
candidato3 = 0
eleitores = int(input("Digite o número de eleitores: "))

for i in range(eleitores):
    voto = int(input("Vote no candidato 1, 2 ou 3: "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1

print(f"Votos para o candidato 1: {candidato1}")
print(f"Votos para o candidato 2: {candidato2}")
print(f"Votos para o candidato 3: {candidato3}")
'''

'''
# Q. 10
numero = int(input("Montar a tabuada de: "))
comeco = int(input("Começar por: "))
fim = int(input("Terminar em: "))

print(f"Vou montar a tabuada de {numero} começando em {comeco} e terminando em {fim}:")
for i in range(comeco, fim + 1):
    print(f"{numero} X {i} = {numero * i}")
'''

# WHILE
'''
# Q. 1
a = -1

while a < 0 or a > 10:
    a = int(input("Digite sua nota: "))
    
    if 0 <= a <= 10:
        print("\nValor válido")
    else:
        print("\nValor inválido")
'''

'''
# Q. 2
user = ''
password = ''

while user == password:
    user = input("Digite seu nome: ")
    password = input("Digite a sua senha: ")

    if user == password:
        print("\nErro! Não use a senha igual o nome de usuário!")
    else:
        print("\nAcesso concedido")
'''

'''
# Q. 3
val = False

while val == False:
    nam = input("Digite o seu nome: ")
    age = int(input("Digite a sua idade: "))
    mon = float(input("Digite o seu salário: R$ "))
    sex = str(input("Sexo (m - masculino / f - feminino): ")).lower()
    stat = str(input("Estado civil (s - solteiro(a) / c - casado(a) / v - viúvo(a) / d - divorciado(a)): "))

    if len(nam) >= 3 and 0 <= age <= 150 and mon > 0 and (sex == 'm' or sex == 'f') and (stat == 's' or stat == 'c' or stat == 'v' or stat == 'd'):
        print("\nInformações validadas")
        val = True
    else:
        print("\nAlguma(s) informação(es) está(ão) incorreta(s)")
        val = False
'''

'''
# Q. 4
a = 80000
b = 200000
year = 0

while a < b:
    a *= 1.03
    b *= 1.015
    year += 1
    
    if a >= b:
        print(f"\nDemorou {year} anos para a cidade A ultrapassar a cidade B")
'''

'''
# Q. 5
year = 0
val = False

while val == False:
    a = int(input("Digite a população da cidade A: "))
    b = int(input("Digite a população da cidade B: "))
    ta = float(input("Digite a taxa de crescimento da cidade A (em porcentagem): "))
    tb = float(input("Digite a taxa de crescimento da cidade B (em porcentagem): "))

    if a >= b:
        print("A população da cidade A já é maior que a população da cidade B, reescreva os valores.")
    else:
        val = True

while a < b:
    a = (a * (ta / 100)) + a
    b = (b * (tb / 100)) + b
    year += 1
    
    if a >= b:
        print(f"\nDemorou {year} anos para a cidade A ultrapassar a cidade B")
        print("Redirecionando novamente para agregação de valores...\n")
        year = 0
        a = int(input("Digite a população da cidade A: "))
        b = int(input("Digite a população da cidade B: "))
        ta = float(input("Digite a taxa de crescimento da cidade A (em porcentagem): "))
        tb = float(input("Digite a taxa de crescimento da cidade B (em porcentagem): "))
'''

'''
# Q. 6
n = int(input("Quantos termos da sequência de Fibonacci deseja? "))
termo1, termo2 = 0, 1
cont = 0

while cont < n:
    print(termo1)
    proximo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo
    cont += 1

'''

'''
# Q. 7
numero = int(input("Digite um número: "))
contador = 0

while numero > 0:
    numero //= 10
    contador += 1

print(f"O número tem {contador} dígitos.")
'''

'''
# Q. 8
senha1 = input("Digite a senha: ")
senha2 = ""

while senha1 != senha2:
    senha2 = input("Repita a senha: ")

print("Senhas coincidem!")
'''

'''
# Q. 9
while True:
    senha = input("Digite uma senha: ")
    
    if len(senha) < 6 or len(senha) > 12:
        print("A senha deve ter entre 6 e 12 caracteres.")
        continue
    
    tem_minuscula = False
    tem_maiuscula = False
    tem_numero = False
    tem_especial = False
    caracteres_especiais = "$#@"
    
    for char in senha:
        if char.islower():
            tem_minuscula = True
        elif char.isupper():
            tem_maiuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in caracteres_especiais:
            tem_especial = True

    if not tem_minuscula:
        print("A senha deve conter pelo menos uma letra minúscula.")
    elif not tem_maiuscula:
        print("A senha deve conter pelo menos uma letra maiúscula.")
    elif not tem_numero:
        print("A senha deve conter pelo menos um número.")
    elif not tem_especial:
        print("A senha deve conter pelo menos um caractere especial ($ # @).")
    else:
        print("Senha válida!")
        break
'''


'''
# Q. 10
soma = 0
numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 para sair): "))

print(f"A soma de todos os números é: {soma}")
'''

'''
# Q. 11
maior = 0
numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    if numero > maior:
        maior = numero
    numero = int(input("Digite um número (0 para sair): "))

print(f"O maior número digitado foi: {maior}")
'''

'''
# Q. 12
total = 0
valor = float(input("Digite o valor do produto (0 para sair): "))

while valor != 0:
    if valor > 0:
        total += valor
    else:
        print("Valor inválido.")
    valor = float(input("Digite o valor do produto (0 para sair): "))

if total > 1000:
    total *= 0.9

print(f"Total a pagar: R$ {total:.2f}")
'''

'''
# Q. 13
soma = 0
cont = 0
numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    soma += numero
    cont += 1
    numero = int(input("Digite um número (0 para sair): "))

if cont > 0:
    media = soma / cont
    print(f"A soma é {soma} e a média é {media:.2f}")
else:
    print("Nenhum número foi digitado.")
'''
