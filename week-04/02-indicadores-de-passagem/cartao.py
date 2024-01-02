meuCartao = int(input("Digite o numero do seu cartao de credito: "))

cartaoLido = 1
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
    cartaoLido = int(input("Digite o numero do proximo cartao de credito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True
        
if encontreiMeuCartaoNaLista:
    print("Ebaaa!! Meu cartao está lá!")
else:
    print("Vish! Nao encontrei poha nenhuma!")