peso_total = 0.0

for x in range(1, 101):

 peso_atual = float(input("Informe o peso da caixa atual:"))

 peso_total = peso_total + peso_atual

 media = peso_total/100

 print("O peso total de caixas é{}. A média de peso é{}".format(peso_total, media))