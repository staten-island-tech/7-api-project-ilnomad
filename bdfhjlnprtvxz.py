import tkinter as tk
from tkinter import ttk
import requests
a=b=c=d=""
def puzzle():
    response = requests.get("https://lichess.org/api/puzzle/next")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    a=data["game"]["perf"]["name"]
    b=data["game"]["clock"]
    c=data["puzzle"]["solution"]
    d=data["game"]["pgn"]
    a_a=ttk.Label(window,text=f"{a},{b},{c},{d}",font=("Helvetica", 14))
    a_a.pack()

window=tk.Tk()
window.geometry('1280x720+320+180')
window.title('Puzzles on LiChess')
outputtext=ttk.Label(window,text="LiChess Puzzles",font=("Helvetica", 14))
outputtext.pack()
button=tk.Button(window,text='Retrieve a puzzle.',command=puzzle)
button.pack(padx=10,pady=10)
window.mainloop()