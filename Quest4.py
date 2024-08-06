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