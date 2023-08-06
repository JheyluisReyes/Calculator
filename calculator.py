type = input("· Please enter the type of operation: ") #+, -, * or /
value1 = float(input("· Please enter the first amount: "))
value2 = float(input("· Please enter the second amount: "))

if type == "+":
    print("")
    print("Result:", value1 + value2)
elif type == "-":
    print("")
    print("Result:", value1 - value2)
elif type == "*":
    print("")
    print("Result:", value1 * value2)
elif type == "/":
    print("")
    print("Result:", value1 / value2)
else:
    print("Sorry, the type of operation is invalid or unrecognized.")
input("")
