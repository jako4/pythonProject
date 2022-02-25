# Calculator that can do all 4 operators and will notify you of type errors

print("")
print("This is a calculator. it's possible to use one of the four arithmetic types: + - * /")
print("")

Use_Calculator: str
Use_Calculator = input("Do you want to use the calculator? Y/N: ")
while Use_Calculator.upper() != "Y" and Use_Calculator.upper() != "N":
    print(" ")
    print("Type N or Y")
    Use_Calculator = input("Do you want to use the calculator? Y/N: ")

if Use_Calculator.upper() == "Y":
    First_number = input("First number ")
    Arithmetic = input("Choose arithmetic type ")
    Second_number = input("Second number ")

    isNumber = First_number.isdigit() and Second_number.isdigit()
    if isNumber:
        First_number = int(First_number)
        Second_number = int(Second_number)

    while isNumber != int and Arithmetic != "+" and Arithmetic != "-" and Arithmetic != "*" and Arithmetic != "/":
        print("")
        print("Try again")
        First_number = input("First number ")
        Arithmetic = input("Choose arithmetic type ")
        Second_number = input("Second number ")
    First_number = int(First_number)
    Second_number = int(Second_number)

    if Arithmetic == "+":
        print(First_number + Second_number)
    elif Arithmetic == "-":
        print(First_number - Second_number)
    elif Arithmetic == "*":
        print(First_number * Second_number)
    elif Arithmetic == "/":
        print(First_number / Second_number)

if Use_Calculator.upper() == "N":
    print("")
    print("You have selected No")
    print("To use the calculator, run the program again")