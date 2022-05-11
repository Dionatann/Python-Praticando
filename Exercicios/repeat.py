#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
#e continue pedindo até que o usuário informe um valor válido.

nota = int(input("informe um número de 1 a 10"))

while nota > 10 or nota < 0:
    print("Valor inválido, insira um valor entre 1 e 10")
    nota = int(input("informe um número de 1 a 10"))