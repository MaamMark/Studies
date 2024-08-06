# QUESTÃO 9 - Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

# Variáveis que esperam receber respectivamente: um valor qualquer e os demais números flutuantes
name = input("Digite o nome do aluno: ")
gradeOne = float(input("Digite a primeira nota: "))
gradeTwo = float(input("Digite a segunda nota: "))
gradeThree = float(input("Digite a terceira nota: "))
# Escrita no console do nome do aluno e sua média aritmética das três notas
print(f"\nA média final do aluno {name} é {(gradeOne + gradeTwo + gradeThree) / 3}")