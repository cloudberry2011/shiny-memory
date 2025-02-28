import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ABQ Data Entry Application")
root.columnconfigure(0, weight=1)

# Start coding here

# Application heading
ttk.Label(
    root,
    text="ABQ Data Entry Application",
    font=("TkDefaultFont", 16)
).grid()

root.mainloop()