import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def scientific_calculator():
    print("Scientific Calculator")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (sqrt)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("0. Exit")

    while True:
        choice = input("Enter operation number (0-9): ")

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            if choice in {'1', '2', '3', '4', '5'}:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Result:", add(num1, num2))
                elif choice == '2':
                    print("Result:", subtract(num1, num2))
                elif choice == '3':
                    print("Result:", multiply(num1, num2))
                elif choice == '4':
                    print("Result:", divide(num1, num2))
                elif choice == '5':
                    print("Result:", power(num1, num2))

            elif choice in {'6', '7', '8', '9'}:
                num = float(input("Enter the number: "))

                if choice == '6':
                    print("Result:", square_root(num))
                elif choice == '7':
                    print("Result:", sin(num))
                elif choice == '8':
                    print("Result:", cos(num))
                elif choice == '9':
                    print("Result:", tan(num))

            else:
                print("Invalid operation number. Try again.")

        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    scientific_calculator()
