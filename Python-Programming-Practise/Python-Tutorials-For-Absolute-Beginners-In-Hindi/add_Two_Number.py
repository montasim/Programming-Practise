#    ------------------------------------------------------------------------------------------
#    Author    : Mohammad Montasim -Al- Mamun Shuvo
#    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
#    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
#    Email     : montasimmamun@gmail.com
#    Github    : https://github.com/montasimmamun/

#    Date      : Created on 17/07/2020
#    Version   : 1.0.1
#    Purpose   : Add two numbwe
#    Input     : Two integer number
#    Output    : Sum of two input
#    ------------------------------------------------------------------------------------------

number1 = input("Enter number1: ")
number2 = input("Enter number2: ")

"""
This will give error because python take input as string.
To get proper output data should be converted from string to int
"""
print(number1, " + ", number2, " = ", (number1 + number2))

"""
Type casting from string to int to get proper output.
This type casting will not work because int(number1 + number2) is typecasting the concatination of number1
and number2 to int. So It is needed to seperately type casting two input. 
"""
print(number1, " + ", number2, " = ", (int(number1 + number2)))

#   type casting from string to int to get proper output
print(number1, " + ", number2, " = ", (int(number1) + int(number2)))
