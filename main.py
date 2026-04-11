import calculator
import tests as t
#All bugs should be fixed
t.tests()
def main():
    print("--- Welcome to the Working Calculator ---")
    
    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
            
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = calculator.add(num1, num2)
            print(f"Result: {result}")
        elif choice == '2':
            result = calculator.subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == '3':
            result = calculator.multiply(num1, num2)
            print(f"Result: {result}")
        elif choice == '4':
            result = calculator.divide(num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
