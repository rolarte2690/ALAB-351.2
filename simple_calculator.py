while True:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    if not num1.isdigit() or not num2.isdigit():
        print("It's not a number, please enter valid numbers!\n")
    else:
        # Valid numbers entered; break out of the loop
        num1 = int(num1)
        num2 = int(num2)
        break

# Now proceed with the operator and calculation
op = input("Choose an operation (+, -, *, /): ")

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif op == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")

else:
    print("Invalid operation selected.")
