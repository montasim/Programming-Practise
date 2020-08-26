 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 26/07/2020
 #    Version   : 1.0.1
 #    Purpose   : Attributes Of Label & Pack
 #    Input     : none
 #    Output    : Attributes Of Label & Pack
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

"""
Important label options
text = adds the text
bd = background
fg = foreground
font = set the fond
padx = x padding
pady = y padding
relief = border styling = SUNKEN, RAISED, GROOVE, RIDGE
"""



#   Program title
root.title("PyCal")
#   display image
guiImage = ImageTk.PhotoImage(Image.open("montasim.jpg"))
imageLebel = Label(image = guiImage)
#   Label() function create label for software
softwareLebel = Label(text="PyCal")
#   pack() function display label
softwareLebel.pack() 
imageLebel.pack()

#   gui logic
#   make gui window interactive
root.mainloop()