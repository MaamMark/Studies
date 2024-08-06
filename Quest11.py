# QUESTÃO 11 - Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar no dia e também a quantidade de dólares disponíveis com o usuário.

# Variáveis que esperam receber valores numéricos flutuantes
price = float(input("Valor da cotação: "))
money = float(input("Quantidade de dólares (US$) disponíveis: "))
#Escrita no console da conversão de dólares para reais
print(f"\nA conversão para reais com a cotação de {price} é de R$ {round(money * price, 2)}") # round() para limitar a quantidade de casas decimais