from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
import TerpHousingHub as logic

def click():
    output_string.set(entry_string.get())
    #logic.find_listing(entry_string.get())

#window
root = ttk.Window(themename = 'morph')
root.title('TerpHousingHub')
root.geometry('800x600')

# title
title_label = ttk.Label(root, text = "Terp Housing Hub", font = 'Calibri 30')
title_label.pack(pady = 10)

# variables
entry_string = tk.StringVar()

#input field
input_frame = ttk.Frame(root, padding = 15)
input_lf = ttk.Labelframe(input_frame, text = "Search for a specific address to find reviews from past tennants or post a review yourself", padding = 15)
#Search field
search_field = ttk.Frame(input_lf)
entry_label = ttk.Label(search_field, text = "Address", width = 8)
entry_label.pack(side=LEFT, padx=(15, 0))
search_entry = ttk.Entry(search_field, textvariable = entry_string)
search_entry.pack(side ='left', fill=X, expand=YES, padx=5)
search_button = ttk.Button(search_field, text='Search', command = click, width = 8)
search_button.pack(side ='left', padx = 5)
search_field.pack(fill=X, expand=YES)
# Browse Options
browse_field = ttk.Frame(input_lf)
or_label = ttk.Label(browse_field, text = "OR", width = 5)
browse_label = ttk.Label(browse_field, text = "Browse for listings", width = 15)
or_label.pack()
browse_label.pack(side='left', padx=(15,0))
browse_field.pack(fill=X, expand=YES)

input_lf.pack(fill=X, anchor=N, expand=YES)
input_frame.pack(fill=BOTH, expand=YES)


#output field
output_frame = ttk.Frame(root)
output_string = ttk.StringVar()
output_label = ttk.Label(output_frame, text = 'Results', font = 'Calibri 15', textvariable = output_string)
output_label.pack()
output_frame.pack(pady = 10)

root.mainloop()