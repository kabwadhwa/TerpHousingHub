from tkinter import *
import tkinter as tk
root = tk.Tk()
root.title('TerpHousingHub')
root.geometry('350x200')
button = tk.Button(root, text = 'Stop', width = 25, command = root.destroy)
button.pack()
root.mainloop()