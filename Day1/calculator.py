#python calculator

operator = input("enter the operator (+ - * /): ")

num1 =float(input("enter the 1st number: "))
num2 =float(input ("enter the 2nd number: "))

if operator == "+" :
    result = num1 +num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1* num2

elif operator == "/":
    result = num1 /num2

print(result)
