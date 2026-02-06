varOne = float(input("Enter your first number:>"))
varTwo = float(input("Enter your second number:>"))

print("I can add, subtract, multiply, divide, exponents, and long division.")
choice = input("What would you like to do?>")

if choice == "add":
    print(varOne + varTwo)
elif choice == "subtract":
    print(varOne - varTwo)
elif choice == "multiply":
    print(varOne * varTwo)
elif choice == "divide":
    print(varOne / varTwo)
elif choice == "exponents":
    print(varOne ** varTwo)
elif choice == "long division":
    print(str(varOne // varTwo) + " r:" + str(varOne % varTwo))
else:
    print("Sorry, I didn't understand that command.")