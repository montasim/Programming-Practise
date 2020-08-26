#    ------------------------------------------------------------------------------------------
#    Author    : Mohammad Montasim -Al- Mamun Shuvo
#    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
#    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
#    Email     : montasimmamun@gmail.com
#    Github    : https://github.com/montasimmamun/

#    Date      : Created on 17/07/2020
#    Version   : 1.0.1
#    Purpose   : Create a faulty calculator
#    Input     : two integer number
#    Output    : matmatical operation. for some specific value it gives incorrect result
#    ------------------------------------------------------------------------------------------

operator = {"+", "-", "*", "/"}
number1 = int(input("Enter number1: "))
print("Available action: ", operator)
action = input("What do you want to do? ")
number2 = int(input("Enter number2: "))

if (number1 == 45):
    if (action == "+"):
        if (number2 == 3):
            print(number1, " + ", number2, " = ", 555)

elif (number1 == 56):
    if (action == "+"):
        if (number2 == 9):
            print(number1, " + ", number2, " = ", 77)
    else:
        if (action == "/"):
            if (number2 == 6):
                print(number1, " / ", number2, " = ", 4)

elif (action == "+"):
    print(number1, " + ", number2, " = ", number1 + number2)

elif (action == "-"):
    print(number1, " - ", number2, " = ", number1 - number2)

elif (action == "*"):
    print(number1, " * ", number2, " = ", number1 * number2)

elif (action == "/"):
    print(number1, " / ", number2, " = ", number1 / number2)

else:
    print("Invalid Input")
