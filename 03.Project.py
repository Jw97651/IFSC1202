first_number = float(input("Enter First Number: "))
operator = input("Enter Operator (+, -, *, /): ")
second_number = float(input("Enter Second Number: "))
if operator == '+':
    result = first_number + second_number
elif operator == '-':
    result = first_number - second_number
elif operator == '*':
    result = first_number * second_number
elif operator == '/':
    if second_number != 0:
        result = first_number / second_number
    else:
        print("Error: Division by zero")
        exit()
else:
    print("Invalid Operator")
    exit()
print(f"{first_number} {operator} {second_number} = {result}")
