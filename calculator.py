# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers

def subtract(a, b):
    return a - b

# Function to multiply two numbers

def multiply(a, b):
    return a * b

# Function to divide two numbers

def divide(a, b):
   if b == 0:
       return"Error! Division by zero"
   else:
       return a / b

def main():
    print("Welcome to Calculator!")

    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your (1/2/3/4/5): ")
        if choice in ("1", "2", "3", "4",):
            a = float(input("Enter a number (a): "))
            b = float(input("Enter a number (b): "))

            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid input. Please enter a valid input.")

if __name__ == "__main__":
    main()
