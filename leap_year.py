# leap_year.py: Checks if a year is leap year.
# Kyriakos, March 6, 2023

import calendar
import tkinter as tk
import tkinter.ttk as ttk

def check():
    value = entry_text.get()
    try:
        if calendar.isleap(int(value)):
            label_text.set("Year " + value + " is leap")
        else:
            label_text.set("Year " + value + " is not leap") 
    except ValueError:
        label_text.set("Please enter a valid year") 
        
window = tk.Tk()
window.title("Leap year check")
window.resizable(False, False)

entry_text = tk.StringVar()
label_text = tk.StringVar()

window.rowconfigure([0, 1, 2, 3], minsize=10, weight=1)
window.columnconfigure(0, minsize=280, weight=1)

lbl = ttk.Label(window, text="Please enter a year:")
lbl.grid(column=0, row=0, padx=5, pady=5)

ent = ttk.Entry(window, textvariable=entry_text)
ent.grid(column=0, row=1, padx=5, pady=5)
ent.focus()

btn = ttk.Button(window, text="Check", command=check)
btn.grid(column=0, row=2, padx=5, pady=5)

lbl_2 = ttk.Label(window, textvariable=label_text, font=("Helvetica 8 bold"))
lbl_2.grid(column=0, row=3, padx=5, pady=5)

window.mainloop()