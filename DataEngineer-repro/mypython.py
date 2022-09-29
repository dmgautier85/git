# This prints text

from cProfile import label
from curses.textpad import Textbox
import tkinter as tk

root = tk.Tk()

root.geometry("800x500")

root.title("My First GUI")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))

label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack()

button = tk.Button(root, text="Click Me Button", font=('Arial', 10))
button.pack(padx=10,pady=10)


# simple comment
#myentry = tk.Entry(root)
#myentry





root.mainloop()
