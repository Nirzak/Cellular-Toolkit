from tkinter import *
import tkinter.ttk as ttk
import Pathloss
import CellStructure

root = Tk()
root.title('Cellular toolkit')


def mainWindow(width, height=200):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screenHeight / 2) + (-100)
    y = (screenHeight / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


mainWindow(700,600)


style = ttk.Style()

def call_CalcPathLoss():
    window1 = Toplevel(root)
    Pathloss.CalcPathLoss(window1)
    return

def call_CalcCell():
    window2 = Toplevel(root)
    CellStructure.CalcCell(window2)
    return

#heading
labelHeading = Label(root,
                     text='Cellular Toolkit',
                     font="-family {Century Gothic} -size 20 -weight bold",
                     background="#1DBC60",
                     foreground="#ffffff"
                     ).place(x=2, y=3, height=44, width=700)

myButton1 = Button(root, text='Calculate Cell Related Info',
                   fg='white',
                   bg='#F56954',
                   relief='flat',
                   command=call_CalcCell,
                   font="-family {Times New Roman} -size 11 -weight bold").place(x=260, y=250, height=30, width=210)

myButton2 = Button(root, text='Caculate Path Loss',
                   fg='white',
                   bg='#F56954',
                   relief='flat',
                   command=call_CalcPathLoss,
                   font="-family {Times New Roman} -size 11 -weight bold").place(x=260, y=300, height=30, width=210)

root.mainloop()
