
def add(first_number, second_number):
    return first_number+second_number

def substract(first_number, second_number):
    return first_number-second_number

def multiply(first_number, second_number):
    return first_number*second_number

def divide(first_number, second_number):
    return first_number/second_number



print("Hello to my calculator")
print("------------------")

while True:

    first_number = int(input("Whats the first number? "))
    second_number = int(input("Whats the second number? "))

    print(f"""
    Choose what operation you want to do
    1 - Add
    2 - Substract
    3 - Multiply
    4 - Divide
    5 - Quit """)

    operation = int(input("> "))

    if operation==1:
        print(add(first_number,second_number))
    elif operation==2:
        print(substract(first_number,second_number))
    elif operation==3:
        print(multiply(first_number,second_number))
    elif operation==4:
        print(divide(first_number,second_number))
    elif operation==5:
        break
    else:
        print("Invalid number")

