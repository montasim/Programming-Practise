 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 26/07/2020
 #    Version   : 1.0.1
 #    Purpose   : Displaying Images Using Label
 #    Input     : none
 #    Output    : Displaying Images Using Label
 #    ------------------------------------------------------------------------------------------


from tkinter import *
from PIL import Image, ImageTk

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
#   display image
guiImage = ImageTk.PhotoImage(Image.open("montasim.jpg"))
softwareLebel = Label(image = guiImage)
#   Label() function create label for software
#   softwareLebel = Label(text="PyCal")
#   pack() function display label 
softwareLebel.pack()

#   gui logic
#   make gui window interactive
root.mainloop()