 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 26/07/2020
 #    Version   : 1.0.1
 #    Purpose   : Label, Geometry, Maxsize & Minsize
 #    Input     : none
 #    Output    : Label, Geometry, Maxsize & Minsize
 #    ------------------------------------------------------------------------------------------


from tkinter import *

#   create base that contain all basic thing
root = Tk()

#   window size
#   widthxheight
root.geometry("544x434")
#   minimum size width, height
root.minsize(434, 544)
#   maximum size width, height
root.maxsize(434, 544)

#   Program Lebel
#   Label() function create label for software
softwareLebel = Label(text="PyCal")
#   pack() function display label 
softwareLebel.pack()

#   gui logic
#   make gui window interactive
root.mainloop()