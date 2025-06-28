
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. exit ")

choice = input("Enter the operation (1/2/3/4/5): ")

if choice == '1':
    result = num1 + num2
    operation = '+'
elif choice == '2':
    result = num1 - num2
    operation = '-'
elif choice == '3':
    result = num1 * num2
    operation = '*'
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        operation = '/'
    else:
        result = "Error: Division by zero!"
        operation = '/'
else:
    result = "Invalid operation selected"
    operation = '?'


if isinstance(result, (int, float)):
    print(f"Result: {num1} {operation} {num2} = {result}")
else:
    print(result)
