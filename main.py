# Function for addition
def add(a, b):
    return a + b


# Function for subtraction
def subtract(a, b):
    return a - b


# Function for multiplication
def multiply(a, b):
    return a * b


# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("float division by zero")
        return None


# Function for power
def power(a, b):
    return a ** b


# Function for remainder
def remainder(a, b):
    if b != 0:
        return a % b
    else:
        print("Error: Division by zero")
        return None


# -------------------------------------
# TODO: Write the select_op(choice) function here
# This function should cover Task 1 (Section 2) and Task 3

def select_op(choice):
    if choice == '+':
        return add
    elif choice == '-':
        return subtract
    elif choice == '*':
        return multiply
    elif choice == '/':
        return divide
    elif choice == '^':
        return power
    elif choice == '%':
        return remainder
    elif choice == '#':
        print("Done. Terminating")
        exit()
    elif choice == '$':
        return -1  
    else:
        print("Unrecognized operation")
        return None


# End the select_op(choice) function here
# -------------------------------------
# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    if choice == '#':
        # Terminate the program
        print("Done. Terminating")
        exit()
    elif choice == '$':
        # Restart the program
        continue

    operation_function = select_op(choice)
    if operation_function == -1:
        # program ends here
        print("Done. Terminating")
        exit()
    
    a = input("Enter first number: ")
    print(a)

    if a == '#':
        # Terminate the program
        print("Done. Terminating")
        exit()
    elif a == '$':
        # Restart the program
        continue

    if not a.isnumeric():
        continue

    b = input("Enter second number: ")
    print(b)

    if b == '#':
        # Terminate the program
        print("Done. Terminating")
        exit()
    elif b == '$':
        # Restart the program
        continue

    if not b.isnumeric():
        continue

    # Check if the operation function is not None
    if operation_function is not None:
        # Convert 'a' and 'b' to float before passing them to the function
        result = operation_function(float(a), float(b))
        print(f"{float(a)} {choice} {float(b)} = {result}")
    else:
        print("Unrecognized operation")
       
