def sum(a, b):
    return a + b

def realDivi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def sub(a, b):
    return a - b

def pow_2_b(b):
    return 2 ** b

if __name__ == "__main__":
    

    while True:
        print("\nChoose operation:")
        print("1. Sum")
        print("2. Real Division")
        print("3. Subtract")
        print("4. Power (2^b)")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = sum(num1, num2)
            print(f"Result: {result}")
        elif choice == '2':
            result = realDivi(num1, num2)
            print(f"Result: {result}")
        elif choice == '3':
            result = sub(num1, num2)
            print(f"Result: {result}")
        elif choice == '4':
            result = pow_2_b(num2)
            print(f"Result: {result}")
        else:
            print("Invalid input. Please enter a valid choice.")
