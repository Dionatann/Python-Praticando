#Function max(), retorna o maior numero entre os 3 numeros
#Function min(), retorna o menor numero entre os 3 numeros
#Ambas funções ja vem icorporada no python
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = max(number1, number2, number3)

print("The largest number is:", largest_number)

#Function round(, faz o arredondamento de numeros float)
income = float(input("Enter the annual income: "))
superior = 85.528

if income < superior:
    tax = round(income - 556.2)
    print("The tax is:", tax, "thalers")
else:
    tax = round(income - 14.839,2)
    print("The tax is:", tax, "thalers")

