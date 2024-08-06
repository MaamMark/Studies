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