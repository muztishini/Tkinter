import tkinter as tk

root = tk.Tk()
root.title("My GUI")
root.geometry('250x50')

label = tk.Label(root, text="Hello world!!!")

label.pack()

root.mainloop()
