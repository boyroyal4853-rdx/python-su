def calculator():
    print(" Simple Calculator")
    print("Options: +  -  *  /")

    a = float(input("first number: "))
    b = float(input("second number "))
    op = input("Operator chosse (+ - * /) = ")

    if op == "+":
        print("Result =", a + b)
    elif op == "-":
        print("Result =", a - b)
    elif op == "*":
        print("Result =", a * b)
    elif op == "/":
        if b != 0:
            print("Result =", a / b)
        else:
            print("Error: Division by Zero")
    else:
        print("Invalid Operator")

calculator()