h = float(input("Informe sua Altura"))
genero = int(input("Informe seu genero, 1 para Homem ou 2 pra Mulher : "))

pesoIdealHomens = (72.7 * h) - 58
pesoIdealMulheres = (62.1 * h) - 44.7

if genero == 1:
    print("Seu peso ideal é", pesoIdealHomens)
elif genero == 2:
    print("Seu peso Ideal é", pesoIdealMulheres)
else:
    print("So é valido os números 1 e 2 para referenciar.")
