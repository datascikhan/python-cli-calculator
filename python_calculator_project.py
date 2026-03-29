# Python Caculator
print("welcome to my new calculator")

# loop start
while True:

    # Menu show
    print("\n Select Operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter choice 1 to 5:")

    # Exit condition
    if choice == '5':
        print("calculator closed")
        break

    # Invalid choice check
    if choice not in ['1', '2', '3', '4']:
        print("Invalid Option, Dubara Try karo")
        continue

    # Input Numbers
    try:
        num1 = float(input("enter first number:"))
        num2 = float(input("enter second number:"))
    except:
        print("sirf number enter karo")
        continue

    # function inside loop
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            return "Error: koi bhe number zero se devide nhi hota hai."
        return a / b
    
    
    # Perform operation
    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")

    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")

