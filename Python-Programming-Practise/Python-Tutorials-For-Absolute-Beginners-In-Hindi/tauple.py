#    ------------------------------------------------------------------------------------------
#    Author    : Mohammad Montasim -Al- Mamun Shuvo
#    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
#    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
#    Email     : montasimmamun@gmail.com
#    Github    : https://github.com/montasimmamun/

#    Date      : Created on 17/07/2020
#    Version   : 1.0.1
#    Purpose   : Demonestrate Tauple
#    Input     : None
#    Output    : Various Tauple operation
#    ------------------------------------------------------------------------------------------

# First bracket is used to define elements of tauple
Grocery = ("Harpic", "Vim Bar", "Soap", "Powder",
           "Tooth Pest", "Water Bottle", "100", "200", "Cloth")
print(Grocery)
print(type(Grocery))
print(Grocery[5])

#   can not got outside index of tauple
#   print(Grocery[9])

Numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(Numbers)
print(type(Numbers))
print(Numbers[7])

#   give start and end index of a tauple
print("0 : 10 =", Numbers[0:10])

#   give start index only. Automatically take end index
print("0 : Empty =", Numbers[0:])

#   give end index only. Automatically take start index
print("Empty : 10 =", Numbers[:10])

#   give no index. Automatically take start and end index
print("Empty : Empty =", Numbers[:])

#   give no index. Automatically take start and end index. By default third value is 1
print("Empty : Empty : Empty =", Numbers[::])

#   give no index. Third index -1 reverse the tauple
print("Empty : Empty : -1 =", Numbers[::-1])

#   give no index. Third index -1 reverse the tauple
print("Empty : Empty : -2 =", Numbers[::-2])

#   give no index. Third index remove one elemen from tauple
print("Empty : Empty : 2 =", Numbers[::2])

#   give no index. Third index remove two elemen from tauple
print("Empty : Empty : 3 =", Numbers[::3])

#   If you want to remove one element you need to give an extra value. Because one extra value is needed
print("Empty : Empty : 3 =", Numbers[::3])


#   find length of a tauple
print("Length:", len(Grocery))

#   find maximum value from a tauple
print("max:", max(Grocery))

#   find minimum value from a tauple
print("min:", min(Grocery))

#   Would not work. Because 10 is int and Numbers is tauple
#   10 * Numbers.append(100)
#   print("append:", Numbers)
