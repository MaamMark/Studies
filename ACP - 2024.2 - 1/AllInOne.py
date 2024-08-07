# QUESTÃO 1 - Solicite ao usuário que insira seu nome e depois imprima uma mensagem de boas-vindas.

# Variável que recebe um valor (qualquer que seja) digitado pelo usuário
name = input("Insira seu nome: ")
# Escrita da saudação no console utilizando a variável anterior
print(f"\nOlá {name}! Seja muito bem vindo")

#--------------------

# QUESTÃO 2 - Peça ao usuário para inserir dois números e imprima a soma, a subtração, a multiplicação e a divisão deles.

# Variáveis que esperam receber dois valores numéricos (em forma "flutuante" caso queira especificar casas decimais) respectivamente determinados pelo usuário
valueOne = float(input("Insira um número: "))
valueTwo = float(input("Insira outro número: "))
# Escrita no console de cada operação matemática, sendo soma, subtração, divisão e multiplicação
print(f"\nA soma dos seus números é: {valueOne + valueTwo}")
print(f"A subtração dos seus números é: {valueOne - valueTwo}")
print(f"A multiplicação dos seus números é: {valueOne * valueTwo}")
print(f"A divisão dos seus números é: {valueOne / valueTwo}")

#--------------------

# QUESTÃO 3 - Crie um programa que solicite ao usuário um número inteiro e imprima o quadrado desse número.

# Variável que espera receber o valor de número inteiro
number = int(input("Digite um número inteiro: "))
# Escrita no console para fornecer o quadrado do número especificado na variável
print(f"\nO quadrado desse número é {number ** 2}")

#--------------------

# QUESTÃO 4 - Faça um programa que o usuário entre com o valor da distância percorrida por um carro em quilômetros e o tempo que ele levou para percorrer essa distância em horas. Encontre a velocidade média e a aceleração média em metros por segundo. Lembrem-se V = d/t e A = V/t. Lembrem-se km/h para m/s basta dividir por 3,6.

# Variáveis que esperam receber respectivamente a distância e o tempo percorridos em forma numérica pelo usuário
distance = float(input("A distância percorrida em KM: "))
time = float(input("O tempo (em horas) para percorrer esta distância: "))
# Fórmulas para conversão da velocidade média (vm) e aceleração média (am)
vm = distance / time
am = (vm / time) / 3.6
# Escrita no console das fórmulas já convertidas em valores
print(f"\nA velocidade média que você teve foi de {vm} Km/h")
print(f"A aceleração média que você teve foi de {round(am, 2)} m/s") # round() limita a quantidade de casas decimais

#--------------------

# QUESTÃO 5 - Faça um programa que o usuário entre com os valores de notas de um aluno de acordo com a tabela a seguir e no final possa apresentar a média final do aluno.
# Nota 1 = Prova 1 + Lista 1
# Nota 2 = Prova 2 + Lista 2
# Média final = (Nota 1 + Nota 2) / 2

# Variáveis que espera receber os valores numéricos que indicam as notas do aluno
valueOne = float(input("Valor da prova 1: "))
valueTwo = float(input("Valor da Lista 1: "))
valueThree = float(input("Valor da prova 2: "))
valueFour = float(input("Valor da Lista 2: "))
# Fórmulas para converter os valores no que é requisitado na questão
gradeOne = valueOne + valueTwo
gradeTwo = valueThree + valueFour
mf = (gradeOne + gradeTwo) / 2
# Escrita no console para mostrar a média final do aluno
print(f"\nA nota final deste aluno é {mf}")

#--------------------

# QUESTÃO 6 - Faça um programa que usuário entre com o valor de um salário de um colaborador e que o programa apresente o salário desse colaborador depois de descontado 15% de imposto e 10% de INSS (aposentadoria).

# Variável que espera receber um número indicando o valor do salário
money = float(input("Digite o valor do salário: R$ "))
# Escrita no console que indica o total do salário final já descontado
print(f"\nSeu salário final é {money - ((money * 0.15) + (money * 0.10))}")

#--------------------

# QUESTÃO 7 - Faça um programa que receba do usuário um valor em metros e forneça o mesmo valor em quilômetros, centímetros e milímetros.

# Variável que espera receber um valor numérico flutuante
value = float(input("Valor em metros a ser convertido: "))
# Escrita no console do valor convertido nas três medidas requisitadas
print(f"\nSeu valor em km: {value / 1000}")
print(f"Seu valor em cm: {value * 100}")
print(f"Seu valor em mm: {value * 1000}")

#--------------------

# QUESTÃO 8 - Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final (depois das comissões) do mês.

# Variáveis que esperam receber respectivamente: qualquer valor (nome pode ser qualquer coisa) e dois números flutuantes em sequência
name = input("Digite o seu nome: ")
money = float(input("Digite o valor do seu salário: "))
sell = float(input("Digite quanto suas vendas renderam: "))
# Escrita no console dos dados requisitados na questão, além da conversão do salário final do vendedor
print(f"\nNome: {name}")
print(f"Salário fixo: {money}")
print(f"Salário final: {(sell * 0.15) + money}")

#--------------------

# QUESTÃO 9 - Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

# Variáveis que esperam receber respectivamente: um valor qualquer e os demais números flutuantes
name = input("Digite o nome do aluno: ")
gradeOne = float(input("Digite a primeira nota: "))
gradeTwo = float(input("Digite a segunda nota: "))
gradeThree = float(input("Digite a terceira nota: "))
# Escrita no console do nome do aluno e sua média aritmética das três notas
print(f"\nA média final do aluno {name} é {(gradeOne + gradeTwo + gradeThree) / 3}")

#--------------------

# QUESTÃO 10 - Imprima na tela as seguintes informações de acordo com os respectivos posicionamentos utilizado apenas um comando de print. Utilize \n para quebra de linha e \t para espaçamento.
# Nome:
#    Idade:
#        Signo:
#            Aniversário:
#        Time:
#    Cidade:
# Sonho:

# Escrita no console conforme requisitado na questão (tudo junto para manter o alinhamento do exemplo)
print("\nNome: Marcos\n\tIdade: 18 anos\n\t\tSigno: Sei lá\n\t\t\tAniversário: 31 de maio de 2006\n\t\tTime: Flamengo\n\tCidade: Altamira\nSonho: Me tornar aquilo...")

#--------------------

# QUESTÃO 11 - Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar no dia e também a quantidade de dólares disponíveis com o usuário.

# Variáveis que esperam receber valores numéricos flutuantes
price = float(input("Valor da cotação: "))
money = float(input("Quantidade de dólares (US$) disponíveis: "))
#Escrita no console da conversão de dólares para reais
print(f"\nA conversão para reais com a cotação de {price} é de R$ {round(money * price, 2)}") # round() para limitar a quantidade de casas decimais

#--------------------

# QUESTÃO 12 - Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a.m.

# Variável que espera receber um número flutuante
value = float(input("Digite o valor do depósito: "))
# Escrita no console indicando qual será o valor após o incremento da taxa de 0,7%
print(f"\nO valor que renderá após um mês é de R$ {(value * 0.007) + value}")

#--------------------

# QUESTÃO 13 - Calcule e imprima a área e o comprimento de uma circunferência. O valor do raio peça ao usuário para digitar.

# Variável que espera um número flutuante
value = float(input("Digite o raio da circunferência: "))
# Escrita no console indicando os valores tanto da circunferência quanto do comprimento (com suas devidadas conversões)
print(f"\nA área dessa circunferência é {2 * 3.14 * value}")
print(f"O comprimento dessa circunferência é {3.14 * (value ** 2)}")

#--------------------

# QUESTÃO 14 - Faça com que uma variável receba seu nome e sobrenome. Após isso, utilizando a concatenação da string, forme três novas palavras.

# Variáveis que esperam receber qualquer valor independentemente do tipo
name = input("Digite o seu nome: ")
lastName = input("Digite o seu sobrenome: ")
# Escrita no console das "novas" três palavras
print(f"\n{name + " " + lastName}")
print((name[0].upper() + lastName[::-1].lower())[:-1]) # .upper() deixa o caractere maiúsculo e .lower o inverso; [::-1] inverte a string e [:-1] remove a última letra
print(lastName[0].upper() + name[::-1].lower())

#--------------------

# QUESTÃO 15 - Solicite ao usuário uma frase e imprima a frase invertida.

# Variável que espera receber qualquer caractere
phrase = input("Digite sua frase: ")
# Escrita no console, a frase invertida
print(f"\n{phrase[::-1]}")

#--------------------

# QUESTÃO 16 - Peça dois números ao usuário e imprima o resultado da potência do primeiro pelo segundo.

# Variáveis que esperam receber dois valores numéricos (em forma "flutuante" caso queira especificar casas decimais) respectivamente determinados pelo usuário
valueOne = float(input("Insira um número: "))
valueTwo = float(input("Insira outro número: "))
# Escrita no console do resultado da potência do primeiro pelo segundo
print(f"\n{valueOne ** valueTwo}")

#--------------------

# QUESTÃO 17 - Peça ao usuário para inserir dois números e imprima o resultado da divisão inteira do primeiro pelo segundo.

# Variáveis que esperam receber dois valores numéricos (em forma "flutuante" caso queira especificar casas decimais) respectivamente determinados pelo usuário
valueOne = float(input("Insira um número: "))
valueTwo = float(input("Insira outro número: "))
# Escrita no console do resultado da divisão inteira do primeiro pelo segundo.
print(f"\n{valueOne // valueTwo}")

#--------------------

# QUESTÃO 18 - Solicite um número ao usuário e imprima "Par" se o número for par, e "Ímpar" se o número for ímpar, sem usar estruturas condicionais ou loops.

# Variável que espera recebe um valor numérico(em forma "flutuante" caso queira especificar casas decimais) determinado pelo usuário
value = float(input("Digite o seu número: "))
# Condicinal indicando que caso o resto do valor ao ser dividido por 2 for 0, ele irá escrever no console "Par"
if value % 2 == 0:
    print("\nPar")
# Caso a condicional acima não for atendida, ele escreverá no console "Ímpar"
else:
    print("\nÍmpar")

#--------------------

# QUESTÃO 19 - Solicite ao usuário que insira seu nome e imprima-o em caixa alta.

# Variável que espera receber qualquer valor
value = input("Digite o seu nome: ")
# Escrita no console do nome em caixa alta
print(f"\n{value.upper()}")

#--------------------

# QUESTÃO 20 - Peça ao usuário que insira uma palavra e imprima a mesma palavra repetida três vezes, sem usar repetições ou estruturas de dados.

# Variável que espera receber qualquer valor
value = input("Digite uma palavra: ")
# Laço de repetição que faz um loop de três ciclos, repetindo a mesma palavra 3 vezes
for x in range(0, 3):
    # Condicional criada para que no primeiro ciclo ele dê um espaço do input (o "\n")
    if x == 0:
        print(f"\n{value}")
    else:
        print(f"{value}")