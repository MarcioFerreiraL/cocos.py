try:
    clienteEspc = (input("É cliente especial? ")).lower()
    if clienteEspc == "sim":
        clienteEspc = True
    else:
        clienteEspc = False

    cocos = int(input("Quantos cocos deseja comprar? "))
    if cocos > 10:
        precoCoco = 2
    elif cocos <= 10:
        precoCoco = 2.5

    valorTotal = cocos*precoCoco

    if clienteEspc == True:
        valorTotal = valorTotal * 0.8

    print(f"O valor total a pagar é: {valorTotal}")
except:
    print("Digite um valor válido!")