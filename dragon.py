import time
import easytemp
import recipe
from recipe import getrecipe
from easytemp import temp9


from tkinter import *

root = Tk()  #makes a blank window, Tk() is a class imported from Tkinter


def tempaccess():
    easytemp.whattemp()
    x = easytemp.temp9

    y = str(x)
    theLabel = Label(root, text=y)
    theLabel.pack()
    root.mainloop()  #keeps the window up, otherwise it would just flash up and close
    easytemp.whattemp()
    x = easytemp.temp9
    y = str(x)
    print("do it another way ", easytemp.whattemp())

def recipeaccess():

    recipelist = recipe.getrecipe()
    print('The recipe is ', recipelist)

# tempaccess()
print("hello1")
recipeaccess()







