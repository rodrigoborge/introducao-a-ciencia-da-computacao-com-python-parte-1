numero = input("Digite um número maior que zero: ")
if int(numero) > 0:
    i = 0
    s = 0
    while i < len(numero):
        s = s + int(numero[i])
        i = i + 1
    print(s)
else:
    print("0")