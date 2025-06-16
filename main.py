num1 = int(input("First Num: "))
num2 = int(input("Second Num: "))
operator = input("operator: ")

def operations():
    if num1 == str:
        print('error')
    if num2 == str:
        print('error')
    if operator == "+":
        print("Sum: ", num1 + num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print("Product: ", num1 / num2)

    elif operator == "%":
        print("Product: ", num1 % num2)

    elif operator == "^":
        print("Product: ", num1 ^ num2)

    elif operator == "<":
        print("Product: ", num1 < num2)

    elif operator == ">":
        print("Product: ", num1 > num2)

    else:
        print("error please try again")
        quit()
        return operations()


operations()
