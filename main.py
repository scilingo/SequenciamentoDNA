lista = []
numero_picos = int(input("Coloque o número de picos a serem lidos: "))

for i in range(numero_picos):
    picos = int(input("Coloque o próximo número: "))
    lista.append(picos)
print("Lista com valor dos picos: ", lista)

for picos, value in enumerate(lista):
    if value == 1:
        lista[picos] = "A"
    elif value == 2:
        lista[picos] = "C"
    elif value == 3:
        lista[picos] = "G"
    elif value == 4:
        lista[picos] = "T"
    else:
        lista[picos] = "X"
print("Lista com os nucleotídeos correspondentes aos picos: ", lista)



