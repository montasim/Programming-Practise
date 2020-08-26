#    ------------------------------------------------------------------------------------------
#    Author    : Mohammad Montasim -Al- Mamun Shuvo
#    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
#    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
#    Email     : montasimmamun@gmail.com
#    Github    : https://github.com/montasimmamun/

#    Date      : Created on 17/07/2020
#    Version   : 1.0.1
#    Purpose   : elif statement Demonestration
#    Input     : None
#    Output    : check age with elif statement
#    ------------------------------------------------------------------------------------------

Age = int(input("Enter Your Age: "))
if (Age > 18):
    print("Your are 18+")

elif (Age == 18):
    print("Your are 18")

else:
    print("You are below 18")
