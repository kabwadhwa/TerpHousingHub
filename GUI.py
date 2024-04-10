from tkinter import *
import tkinter as tk

#window
root = tk.Tk()
root.title('TerpHousingHub')
root.geometry('750x600')

# title
title_label = Label(root, text = "Terp Housing Hub", font = 'Calibri 30')
title_label.pack()

#input field
input_frame = Frame(root)
search_label = Label(input_frame, text = "Search for a specific address to find reviews from past tennants or post a review yourself", font = 'Calibri 15')
search_entry = Entry(input_frame)
search_button = Button(input_frame, text='Search')
search_label.pack()
search_entry.pack()
search_button.pack()
input_frame.pack()



root.mainloop()