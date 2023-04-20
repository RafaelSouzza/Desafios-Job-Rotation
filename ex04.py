valores = {
    "valor_SP": 67836.43,
    "valor_RJ": 36678.66,
    "valor_MG": 29229.88,
    "valor_ES": 27165.48,
    "valor_Outros": 19849.53
}
valor_Total = 0
x = 0
for val in valores.values():
    valor_Total += val
for val in valores.values():
    x = (100*val) / valor_Total
    print("O valor R${} representa o equivalente {:.2f}% do valor total".format(val, x))
