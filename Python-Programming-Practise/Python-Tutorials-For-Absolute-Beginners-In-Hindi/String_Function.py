#    ------------------------------------------------------------------------------------------
#    Author    : Mohammad Montasim -Al- Mamun Shuvo
#    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
#    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
#    Email     : montasimmamun@gmail.com
#    Github    : https://github.com/montasimmamun/

#    Date      : Created on 17/07/2020
#    Version   : 1.0.1
#    Purpose   : Demonestrate various string function
#    Input     : None
#    Output    : Various String operation
#    ------------------------------------------------------------------------------------------

String = "This is a string."

#   Print String variable
print("Actual String:", String, "\n")

#   print a character from a string variable
print("Prind Index 1:", String[1], "\n")

#   print a portion from a string variable. 0 is starting index 5-1 is last index
print("Print index 0 - 5:", String[0:5], "\n")

"""
if you do not give any index it will automatically start from starting index to last index 
and will give actual output
"""
print("No Papametes:", String[:], "\n")

#   lenght of a string
print("Length is:", len(String), "\n")

#   can not print outside of string index
#   print(String[80], "\n")

#   can not print outside of string index, but can print from starting index to given index
print("Index 0 - outside String index:", String[0:80], "\n")

#   This will give the actual string
print("Start:End:Default=", String[0:18:1], "\n")

#   print the string and escape one character continuously.
print("Start:End:Escape 1 Char=", String[0:18:2], "\n")

#   if you want to escape two character contiously you nedd to include 3 as third parameter.
print("Start:End:Escape 2 Char=", String[0:18:3], "\n")

#   so if you want to escape character you nedd to add one extra value as third parameter
print("Start:End:Escape 3 Char=", String[0:18:4], "\n")

#   if you do not give starting index it will automatically start from index 0
print("Empty:End=", String[:18], "\n")

#   if you do not give ending index it will automatically end at last index
print("Start:Empty=", String[0:], "\n")

"""
if you do not give any index it will automatically start from starting index to last index 
and will give actual output
"""
print("::=", String[::], "\n")

#   if you do not give ending index it will automatically start from 0 to last index and escape 1 character
print("::2=", String[::2], "\n")

"""
if you do not give ending index it will automatically start from 0 to last index and escape 99 character.
First Character will always be printed
"""
print("::99=", String[::99], "\n")

#   This will not work
#   print("This is another string.", [0:17:2])


#   Negative index of string,. Won't print. -1 to 0 has nothing
print("-1:0=", String[-1:0])

#   Negative index of string,. -5 to 1 has ring. Dot(.) will remove. Last index would not be printed.
print("-5:1=", String[-5:-1])

#   Negative index of string,. 12 to 1 has ring. Dot(.) will remove. Last index would not be printed.
print("12:-1=", String[12:-1])


#   -1 as third parameter will reverse the string
print("::-1=", String[::-1])

#   -2 as third parameter will reverse the string and remove 1 character
print("::-2=", String[::-2])

# type of variable
print("Type:", type(String))

"""
isalnum() function check if it is a number. if then return True. else False
if a string has white space in it. isalnum will return false.
"""
print("isalnum:", String.isalnum())

"""
isalnum() function check if it is a number. if then return True. else False
if a string has white space in it. isalnum will return false. This time it has no white space to it will 
print true
"""
Name = "YourName"
print("isalnum:", Name.isalnum())

"""
isalnum() function check if it is a Alpha Neumeric Number. if then return True. else False
if a string has white space in it. isalpha will return false.
"""
print("isalpha:", String.isalpha())

#   endswith() function will check if it is end with the given string. if then return True. else false.
#   endswith() function is case sensitive
print("endswith:", String.endswith("string."))
print("endswith:", String.endswith("String."))


#   count() function will count the given string. Returns the number of how many times it is there
print("count i:", String.count("i"))

#   capitalize() function make first letter capital of a string
Author = "me"
print("capatalize:", Author.capitalize())

#   find() function finds the given string in the string
print("find:", String.find("is"))

#   lower() function make every character lowercase
First = "YourFIRSTNAME"
print("lower:", First.lower())

#   upper() function make every character uppercase
Last = "yourlastname"
print("upper:", Last.upper())

#   replace() function replace string value with given value
print("replace:", String.replace("This is a", "These are some"))
