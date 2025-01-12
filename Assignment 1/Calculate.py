def calculator():
    print("Welcome to the Basic Calculator!")
    
    
    num1 = 10       
    num2 = 5        
    operation = '+' 
    
    print(f"Inputs: {num1}, {num2}, {operation}")
    
    # Perform the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation. Please use +, -, *, or /.")


calculator()
