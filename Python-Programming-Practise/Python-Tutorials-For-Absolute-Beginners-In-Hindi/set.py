#    ------------------------------------------------------------------------------------------
#    Author    : Mohammad Montasim -Al- Mamun Shuvo
#    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
#    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
#    Email     : montasimmamun@gmail.com
#    Github    : https://github.com/montasimmamun/

#    Date      : Created on 17/07/2020
#    Version   : 1.0.1
#    Purpose   : Set Demonestration
#    Input     : None
#    Output    : Various Set Operation
#    ------------------------------------------------------------------------------------------

s = set()
print(type(s))

s_from_list = set([1, 2, 3, 4, 5])
print(s_from_list)
print(type(s_from_list))

#   add() is used to add elements to set
s.add(1)
print("add:", s)

#   can not add same value to set
s.add(1)
print("add:", s)

#   add() function add value at the end of set
s.add(2)
print("add:", s)

#   union() function add all unique values to set
s1 = s.union({3, 4, 5})
print("union:", s1, s)

#   intersection() function add all common values to set
s1 = s1.intersection({3, 4})
print("intersection:", s1, s)

#   len() function prints lenght of a set
print("len:", len(s1))

#   min() function prints min value of a set
print("min:", min(s1))

#   max() function prints max value of a set
print("max:", max(s1))

#   remove() function prints max value of a set
s1.remove(4)
print("remove:", s1)
