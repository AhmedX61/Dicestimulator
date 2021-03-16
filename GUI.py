from tkinter import *
from tkinter import ttk
from random import randint

#Global Variables
window = Tk()
window.title('Dice Simulator')
style = ttk.Style()
style.theme_use('winnative')

#Add Buttons
Bu1 = ttk.Button(window, text=' ')
Bu1.grid(row=0, column=0, sticky='snew', ipadx=100, ipady=100)
Bu1.state(['disabled'])

Bu2 = ttk.Button(window, text='Dice')
Bu2.grid(row=1, column=0, sticky='snew', ipadx=10, ipady=20)
Bu2.config(command=lambda: Again())

def Again():
    SetLayout()

def SetLayout():
    ID = randint(1, 6)
    if ID == 1:
        Bu1.config(text="-----------\n|          |\n|    O    |\n|          |\n-----------")
    elif ID == 2:
        Bu1.config(text="-----------\n|             |\n| O     O |\n|             |\n-----------")
    elif ID == 3:
        Bu1.config(text="-----------\n|    O    |\n|    O    |\n|    O    |\n-----------")
    elif ID == 4:
        Bu1.config(text="-----------\n| O     O |\n|             |\n| O     O |\n-----------")
    elif ID == 5:
        Bu1.config(text="-----------\n| O     O |\n|     O     |\n| O     O |\n-----------")
    elif ID == 6:
        Bu1.config(text="-----------\n| O     O |\n| O     O |\n| O     O |\n-----------")


window.mainloop()