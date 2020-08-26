#    ------------------------------------------------------------------------------------------
#    Author    : Mohammad Montasim -Al- Mamun Shuvo
#    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
#    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
#    Email     : montasimmamun@gmail.com
#    Github    : https://github.com/montasimmamun/

#    Date      : Created on 17/07/2020
#    Version   : 1.0.1
#    Purpose   : Demonestrate for loop
#    Input     : An integer number
#    Output    : Iterate loop according to integer
#    ------------------------------------------------------------------------------------------

#   for loop works on list
nameList = ["Loop", "Carry", "Array", "While", "Do", "Break", "Continue"]
print("List:------------------------------------------------------------------------------")
for i in nameList:
    print(i)

print("\n")

#   for works on list of list
listOfList = [["Loop", 1], ["Carry", 2], ["Array", 4], [
    "While", 5], ["Do", 6], ["Break", 7], ["Continue", 8]]
print("List of List:----------------------------------------------------------------------")
for i in listOfList:
    print(i)

print("\n")

#   for can print item only
listOfList = [["Loop", 1], ["Carry", 2], ["Array", 4], [
    "While", 5], ["Do", 6], ["Break", 7], ["Continue", 8]]
print("Item of List:----------------------------------------------------------------------")
for i, item in listOfList:
    print(i)

print("\n")

#   for can print value only
listOfList = [["Loop", 1], ["Carry", 2], ["Array", 4], [
    "While", 5], ["Do", 6], ["Break", 7], ["Continue", 8]]
print("Value of List:----------------------------------------------------------------------")
for i, value in listOfList:
    print(value)

print("\n")

#   for can print both item and value
listOfList = [["Loop", 1], ["Carry", 2], ["Array", 4], [
    "While", 5], ["Do", 6], ["Break", 7], ["Continue", 8]]
print("Item and Value of List:----------------------------------------------------------------------")
for i, value in listOfList:
    print(i, value)

print("\n")

#   for loop works on tauple
nameList = ("Loop", "Carry", "Array", "While", "Do", "Break", "Continue")
print("Tauple:----------------------------------------------------------------------------")
for i in nameList:
    print(i)

print("\n")

#   for loop works on dictionary
dictionaryList = dict(listOfList)
print(dictionaryList)
for item in dictionaryList:
    print(item)

print("\n")

#   this will give error. can not works for value of dictionary. to solve this items() function is used
"""
for item, value in dictionaryList:
    print(value)

print("\n")
"""

#   items() function will print value from dictionary
for item, value in dictionaryList.items():
    print(value, item)
