import tkinter as tk


def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()
root.title("My GUI")
root.geometry('250x50')

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Quit", fg="red", command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame, text="Hello",fg="green", command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
