# QUESTÃO 18 - Solicite um número ao usuário e imprima "Par" se o número for par, e "Ímpar" se o número for ímpar, sem usar estruturas condicionais ou loops.

# Variável que espera recebe um valor numérico(em forma "flutuante" caso queira especificar casas decimais) determinado pelo usuário
value = float(input("Digite o seu número: "))
# Condicinal indicando que caso o resto do valor ao ser dividido por 2 for 0, ele irá escrever no console "Par"
if value % 2 == 0:
    print("\nPar")
# Caso a condicional acima não for atendida, ele escreverá no console "Ímpar"
else:
    print("\nÍmpar")