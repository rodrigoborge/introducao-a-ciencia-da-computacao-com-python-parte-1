x = int(input("Escreva um número: "))
soma = 0
while (x != 0):
    resto = x % 10
    x = (x - resto)//10
    soma = soma + resto
print("A soma dos números digitados é:",soma)