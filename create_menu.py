from tkinter import *
from tkinter.filedialog import askopenfilename


def new_file():
    print("New File!")


def open_file():
    name = askopenfilename()
    print(name)


def about():
    print("This is a simple example of a menu")


root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open...", command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="about...", command=about)

mainloop()
