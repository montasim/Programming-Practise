#    ------------------------------------------------------------------------------------------
#    Author    : Mohammad Montasim -Al- Mamun Shuvo
#    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
#    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
#    Email     : montasimmamun@gmail.com
#    Github    : https://github.com/montasimmamun/

#    Date      : Created on 17/07/2020
#    Version   : 1.0.1
#    Purpose   : Demonestrate Dictionary
#    Input     : None
#    Output    : Various Dictionary operation
#    ------------------------------------------------------------------------------------------

#    Dictionary is case sensitive. Key of dictionary is immutable
FoodList = {"Breakfast": "Rooti", "Lunch": "Rice", "Dinner": "Rice"}

print(FoodList)
print(type(FoodList))

#   Dictionary inside a dictionary
YourFood = {"Breakfast": {"Rooti": "Corn powder",
                          "Vegitables": "Potato, Tomato"}, "Lunch": "Rice", "Dinner": "Rice"}
print(YourFood)
print(YourFood["Breakfast"]["Rooti"])

#   Add elements to existing dictionary. Elements will be added to last
FoodList["Light Food"] = "Bread, tea"
print(FoodList)

#   access elements of dictionary
print(FoodList["Dinner"])

#   Will give an error
#   print(FoodList[2])

#   Change value of existing dictionary
FoodList["Light Food"] = "Soup, Tea"
print(FoodList)

#   Change value of key of dictionary
FoodList["Evening Food"] = "Soup, Tea"
print(FoodList)

#   Change value of key of dictionary
FoodList["100"] = "Soup, Tea"
print(FoodList)

#   del keyword is used to delete key of dictionary
del FoodList["100"]
print(FoodList)

#   copy() function is used to copy a dictionary
print("copy:", YourFood.copy())
MyFood = YourFood
print("MyFood:", MyFood)

"""
After copy a dictionary using assignment operator it just point that operator.
So any change to parent or child will affect both
Copy() function is used to solve this problem
"""
del MyFood["Lunch"]
print("MyFood:", MyFood)
print("YourFood:", YourFood, "\n")

#   copy() function coppies a dictionary
OurFood = MyFood.copy()
print("OurFood:", OurFood)
del OurFood["Dinner"]
print("OurFood", OurFood)
print("MyFood", MyFood)
print("YourFood", YourFood, "\n")

#   get() function is used to get a key value of dictionary
print(OurFood.get("Breakfast"))

#   this gives a error
#   print(OurFood.get({"Breakfast": "Rotti"}))

#   update() function is used to add elements to dictionary
OurFood.update({"Dinner": "Rice"})
print(OurFood)

#   keys() function is used to print keys of a dictionary
print(OurFood.keys())

#   items() function is used to print key, value pairs of a dictionary
print(OurFood.items())
