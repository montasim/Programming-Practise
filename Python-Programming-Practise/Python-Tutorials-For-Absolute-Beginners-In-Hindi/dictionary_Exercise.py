#    ------------------------------------------------------------------------------------------
#    Author    : Mohammad Montasim -Al- Mamun Shuvo
#    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
#    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
#    Email     : montasimmamun@gmail.com
#    Github    : https://github.com/montasimmamun/

#    Date      : Created on 17/07/2020
#    Version   : 1.0.1
#    Purpose   : Find value for keys
#    Input     : Key
#    Output    : Value
#    ------------------------------------------------------------------------------------------

NameDictionary = {"C": "Dennis Ritchie", "Java": "James Gosling",
                  "C++": "Bjarne Stroustrup", "Python": "Guido van Rossum", "PHP": "Rasmus Lerdorf",
                  "Perl": "Larry Wall", "JavaScript": "Brendan Eich", "Ruby": "Yukihiro Matsumoto",
                  "Lisp": "John McCarthy", "Pascal": "Niklaus Wirth"}

print("Any one of these:")
print(NameDictionary.keys(), end="\n")

Key = input("Language name: ")
Key = Key.capitalize()

print("Creator Name:", NameDictionary.get(Key))
