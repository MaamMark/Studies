# QUESTÃO 14 - Faça com que uma variável receba seu nome e sobrenome. Após isso, utilizando a concatenação da string, forme três novas palavras.

# Variáveis que esperam receber qualquer valor independentemente do tipo
name = input("Digite o seu nome: ")
lastName = input("Digite o seu sobrenome: ")
# Escrita no console das "novas" três palavras
print(f"\n{name + " " + lastName}")
print((name[0].upper() + lastName[::-1].lower())[:-1]) # .upper() deixa o caractere maiúsculo e .lower o inverso; [::-1] inverte a string e [:-1] remove a última letra
print(lastName[0].upper() + name[::-1].lower())