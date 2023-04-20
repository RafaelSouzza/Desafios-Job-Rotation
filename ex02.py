array = []
array.append(0)
array.append(1)

valor = int(input("Digite o valor para saber se pertence a sequência de Fibonacci: ")) # entrada do valor

for i in range(2,valor):
    num1 = i - 1 # O número anterior
    num2 = i - 2 # O número anteanterior 
    somaFib = array[num1] + array[num2]
    array.append(somaFib)
    if(somaFib > valor):
        break
    
if(valor not in array):
    print("O valor {} não pertence a sequência de Fibonacci".format(valor))
else:
    print("O valor {} pertence a sequência de Fibonacci".format(valor))