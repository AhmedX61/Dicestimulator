from tkinter import *
from tkinter import ttk
from random import randint

#Global Variables
number = randint(1,6)
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
Bu2.config(command=lambda: SetLayout(number))


def Playnumber():

    if number == 1:
        print("-----------")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("-----------")
    if number == 2:
        print("-----------")
        print("|         |")
        print("| O     O |")
        print("|         |")
        print("-----------")
    if number == 3:
        print("-----------")
        print("|    O    |")
        print("|    O    |")
        print("|    O    |")
        print("-----------")
    if number == 4:
        print("-----------")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print("-----------")
    if number == 5:
        print("-----------")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print("-----------")
    if number == 6:
        print("-----------")
        print("| O     O |")
        print("| O     O |")
        print("| O     O |")
        print("-----------")

def SetLayout(ID):

    if ID == 1:
        Bu1.config(text="-----------\n|         |\n|    O    |\n-----------\n|         |")
    elif ID == 2:
        Bu1.config(text="-----------\n|         |\n|    O    |\n-----------\n|         |")
    elif ID == 3:
        Bu1.config(text="-----------\n|         |\n|    O    |\n-----------\n|         |")
    elif ID == 4:
        Bu1.config(text="-----------\n|         |\n|    O    |\n-----------\n|         |")
    elif ID == 5:
        Bu1.config(text="-----------\n|         |\n|    O    |\n-----------\n|         |")
    elif ID == 6:
        Bu1.config(text="-----------\n|         |\n|    O    |\n-----------\n|         |")


window.mainloop()