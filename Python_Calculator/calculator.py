def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


while True:
    print("\n===== Python CLI Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = addition(num1, num2)
            print("Result:", result)

        elif choice == "2":
            result = subtraction(num1, num2)
            print("Result:", result)

        elif choice == "3":
            result = multiplication(num1, num2)
            print("Result:", result)

        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = division(num1, num2)
                print("Result:", result)

    else:
        print("Invalid choice. Please try again.")