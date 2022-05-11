#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
#diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
#regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que
#João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesoPeixe = float(input("informe o peso dos peixe :"))
kgPeixe_Limite = int(50)
multa = int(4)

if pesoPeixe > kgPeixe_Limite:
    pesoTotalComMulta = (pesoPeixe - kgPeixe_Limite) * 4
    print("O peso dos peixes passou do limite permitido, será comprado um valor de R$ 4,00 a cada Kg acima do permitido.")
    print("O valor da Multa será de R$", pesoTotalComMulta )
else:
    print("O peso dos peixes é menor que o Limite permitindo, sendo assim seu peso total é de", pesoPeixe, "kg")