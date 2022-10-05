from tkinter import *
from tkinter.colorchooser import askcolor


def callback():
    result = askcolor(color="#6a9662", title="Bernd's Color Chooser")
    print(result)


root = Tk()
Button(root, text='Choose Color', fg="dark green", command=callback).pack(side=LEFT, padx=10)
Button(text='Quit', command=root.quit, fg="red").pack(side=LEFT, padx=10)
mainloop()
