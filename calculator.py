# python program to create a simple calculator

#function for add two number
def add(num1, num2):
    return num1 + num2

#function for substract two number
def sub(num1, num2):
    return num1 - num2

#function for multiply two number
def multiply(num1, num2):
    return num1 * num2

#function for divide two number
def divide(num1, num2):
    return num1 / num2

#function for average two number
def avg(num1, num2):
    return (num1 + num2)/2

print("please select a operation:\n" \
      "1. Addition\n"\
      "2. Subtraction\n"\
      "3. Multiplication\n"\
      "4. Division\n"\
      "5. Average\n")

select = int(input("Select a operation from 1,2,3,4,5: "))

number1 = int(input("Enter firt number: "))
number2 = int(input("Enter second number: "))

if select == 1:
    print(number1, "+", number2, "= ", \
          add(number1, number2))
    
elif select == 2:
    print(number1, "-", number2, "= ", \
          sub(number1, number2))
    
elif select == 3:
    print(number1, "*", number2, "= ", \
          multiply(number1, number2))
    
elif select == 4:
    print(number1, "/", number2, "= ", \
          divide(number1, number2))
    
elif select == 5:
    print("(", number1, "+", number2, ")", "/", "2", "= ", \
          avg(number1, number2))
    
else:
    print("Invalid operation! pls select again!")