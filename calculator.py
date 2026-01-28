#Calculator program for quiz 2

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

if __name__ == "__main__":
    print("Simple Calculator")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+ or -): ")

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    else:
        print("Invalid operation")
        exit(1)
    
    print(f"The result is: {result}")

# End of calculator program