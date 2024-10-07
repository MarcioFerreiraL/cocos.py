try:
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite sua peso(kg): "))
    imc = peso/(altura*2)
    if imc < 18.5:
        print("Baixo peso")
    elif 24.9 > imc > 18.6:
        print("Peso normal")
    elif 29.9 > imc > 25:
        print("Sobrepeso")
    elif 34.9 > imc > 30:
        print("Obesidade grau I")
    elif 39.9 > imc > 35:
        print("Obesidade grau II")
    elif imc > 40:
        print("Obesidade grau III")
    else: 
        print("Erro!")
except:
    print("Digite valores válidos!")