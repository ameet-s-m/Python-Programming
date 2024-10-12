def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x,y):
    return x % y

print("Welcome to calculator, Thanks for using our calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")

while True:
    choice = input("Enter your choice (1 or 2 or 3 or 4 or 5): ")
    if choice in ('1', '2', '3', '4', '5'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        if choice == '1':
            print(number1, "+", number2, "=", add(number1, number2))
        elif choice == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))
        elif choice == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))
        elif choice == '4':
            print(number1, "/", number2, "=", divide(number1, number2))
        elif choice == '5':
            print(number1, "%", number2, "=", modulo(number1, number2))    
        break
    else:
        print("Invalid input. Please choose a valid operation.")