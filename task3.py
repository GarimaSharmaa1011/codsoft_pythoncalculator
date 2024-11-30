def calculator():
    print("Welcome to the Simple Calculator!")

    while True:
        try:
            
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
          
            print("\nChoose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            
            choice = input("Enter your choice (1/2/3/4): ")
            
          
            if choice == "1":
                result = num1 + num2
                operation = "+"
            elif choice == "2":
                result = num1 - num2
                operation = "-"
            elif choice == "3":
                result = num1 * num2
                operation = "*"
            elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    operation = "/"
                else:
                    print("Error: Division by zero is not allowed.")
                    continue
            else:
                print("Invalid choice. Please try again.")
                continue

            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue
        
      
        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for using the calculator! Goodbye!")
            break

if __name__ == "__main__":
    calculator()
