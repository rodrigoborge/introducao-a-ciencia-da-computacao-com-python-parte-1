numero = int(input("Fatorial de: "))
resultado = 1
cont = 1
while cont <= numero:
    resultado *= cont
    cont += 1
print("O fatorial de",numero,"é:",resultado)