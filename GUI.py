from tkinter import *
from tkinter import ttk
import PIL.ImageTk
from random import randint

#Global Variables
window = Tk()
window.title('Dice Simulator')
window.geometry("400x400")
style = ttk.Style()
style.theme_use('winnative')

#Add Items
pic1 = "F:\Githup\Dicestimulator\die1.PNG"
p1 = PIL.Image.open(pic1)
photo = PhotoImage(file = "F:\Githup\Dicestimulator\die1.PNG")

label = ttk.Label(window, image=photo)
label.pack()

button = ttk.Button(window, text='Dice')
button.grid(row=0, column=0, sticky='snew')
button.config(command=lambda: Again())
button.pack()


def Again():
    SetLayout()

def SetLayout():
    ID = randint(1, 6)
    if ID == 1:
        label.config(text="-----------\n|          |\n|    O    |\n|          |\n-----------")
    elif ID == 2:
        label.config(text="-----------\n|             |\n| O     O |\n|             |\n-----------")
    elif ID == 3:
        label.config(text="-----------\n|    O    |\n|    O    |\n|    O    |\n-----------")
    elif ID == 4:
        label.config(text="-----------\n| O     O |\n|             |\n| O     O |\n-----------")
    elif ID == 5:
        label.config(text="-----------\n| O     O |\n|     O     |\n| O     O |\n-----------")
    elif ID == 6:
        label.config(text="-----------\n| O     O |\n| O     O |\n| O     O |\n-----------")


window.mainloop()