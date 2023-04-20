palavra = str(input("Digite uma palavra que será invertida: "))
palavra_Separada = list(palavra)
palavra_Invertida = ""
for n in range(len(palavra_Separada)-1, -1, -1):
    palavra_Invertida += str(palavra_Separada[n])
print("A palavra {} invertida ficará {}".format(palavra, palavra_Invertida))