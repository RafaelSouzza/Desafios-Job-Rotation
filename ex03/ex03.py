# -*- coding: UTF-8 -*-
import json
data_JSON = open("./ex03/faturamento.json")
data_JSON = data_JSON.read()
data_dict = json.loads(data_JSON)
maior, menor, valor_Total, qtd_dias, media_dias = 0, 0, 0, 0, 0

for val in data_dict["faturamento"]:
    valor = val["valor"]
    valor_Total += valor
    if(valor > maior):
        maior = valor
    if(valor < menor and valor != 0 or menor == 0):
        menor = valor
    if(valor != 0):
        qtd_dias += 1
        
media = valor_Total / qtd_dias 
 
for val in data_dict["faturamento"]:
    valor = val["valor"]
    if(valor > media):
        media_dias += 1
    
print("A média mensal é R${:.2f}, o maior valor desse mês R${} e o menor R${} e o número de dias que superaram a média mensal foram {}.".format(media, maior, menor, media_dias))