# Python calculator
operator = input("Enter operator (+, -, *, / ) : ")
num1 = float(input("Enter the 1stnumber: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = (num1 + num2)
    print(round(result,2))
elif operator == "-":
    result = (num1 - num2)
    print(round(result,2))
elif operator == "*":
    result = (num1 * num2)
    print(round(result,2))
elif operator == "/":
    result = (num1 / num2)
    print(round(result,2))
else:print(f"The operator {operator} is not valid")
