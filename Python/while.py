secret_number = 777

number = int(input("Please, insert the number "))

while number != secret_number:
    "Ha ha! You're stuck in my loop!"
    number = int(input("Please, insert the number "))
    if number == secret_number:
        print(secret_number)
        print("Well done, muggle! You are free now.")
