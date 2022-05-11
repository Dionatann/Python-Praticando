#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

porHora = float(input("Informe quanto você ganha por hora :"))
numeroHoraDia = float(input("Informe o número de horas trabalhada no Dia :"))
numeroHoraMes = numeroHoraDia * 30

salarioMes = porHora * numeroHoraMes
ir = 11.0/100
inss = 8.0 / 100
sindicato = 5.0 / 100
descontos = ir + inss + sindicato
salarioDescontoTotal = salarioMes - (descontos * salarioMes)

print(descontos)
#salário bruto.
print("Seu salário Bruto é de", salarioMes)

#quanto pagou ao INSS.
print("Seu salário com desconto de INSS",salarioMes - inss)

#quanto pagou ao sindicato.
print("Seu salário com desconto do sindicato",salarioMes - sindicato)

#o salário líquido.
print("Seu salário líquido é de", salarioDescontoTotal)

#calcule os descontos e o salário líquido, conforme a tabela abaixo:
print("Seu salário com desconto é de", salarioDescontoTotal)
