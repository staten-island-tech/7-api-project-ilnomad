import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('1280x720+320+180')
root.title('Entry Widget Demo')


name_entry = ttk.Entry(root)
name_entry.pack(pady=5)
name_entry.focus()

email_entry = ttk.Entry(root)
email_entry.pack(pady=5)

root.mainloop()