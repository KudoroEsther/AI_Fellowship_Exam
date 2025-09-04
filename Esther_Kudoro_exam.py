#QUESTION 1
#Basic Calculator

#Defining each operation
def addition(num1, num2):
    return f"Result: {num1+num2}"

def subtraction(num1, num2):
    return f"Result: {num1 - num2}"

def multiplication(num1, num2):
    return f"Result: {num1*num2}"

def division(num1, num2):
    if num2 != 0:
        return f"Result: {num1/num2}"
    else:
        print("You cannot divide by zero")

#Accepting input
try: 
    while True:
        num1 = float(input("\nEnter your first number: "))
        num2 = float(input("Enter your second number: "))

        operation = input("\nChoose an operation (+, -, *, /) or 'exit' to quit: ").lower().strip()

        if operation == "+":
            print(addition(num1, num2))

        elif operation == "-":
            print(subtraction(num1, num2))
        
        elif operation == "*":
            print(multiplication(num1, num2))

        elif operation == "/":
            print(division(num1, num2))

        elif operation == "exit":
            print("Closing calculator...")
            break
        else:
            print("Invalid option, try again.")
            continue

except ZeroDivisionError:
    print("Your cannot divide by zero.")
except ValueError as v:
    print("Error", v)
except TypeError as t:
    print("Error", t)
except Exception as e:
    print("Error", e)



#QUESTION 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ").lower()
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd")



#QUESTION 3
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break
    
    try:
        if int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")