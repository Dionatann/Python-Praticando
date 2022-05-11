#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
# de latas de tinta a serem compradas e o preço total.

tamanhoEmMetrosQuadrado = float(input("Informe os metros quadrados da parede a ser pintada :"))
quantidadeTintaIdeal = tamanhoEmMetrosQuadrado / 3
tintaLata = int(18) #litros
precoLataTinta= float(80.0) #preço
umaLataTinta = tintaLata / 3

totalLataTinta = int(quantidadeTintaIdeal * umaLataTinta)
precoLataTotal = totalLataTinta * precoLataTinta

print("A quantidade de latas recomendada para", tamanhoEmMetrosQuadrado, "metros quadrado é de", totalLataTinta, "latas de tinta")
print("O valor a pagar será de R$", precoLataTotal)