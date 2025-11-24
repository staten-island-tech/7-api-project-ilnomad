import tkinter as tk
from tkinter import ttk
import requests

def puzzle():
    response = requests.get("https://lichess.org/api/puzzle/daily")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    return{
        "Gamemode": data["game"]["perf"]["name"],
        "Clock": data["game"]["clock"],
        "Solution": data["puzzle"]["solution"],
        "PGN": data["game"]["pgn"]
    }
print(puzzle())

awindow = tk.Tk()
awindow.geometry('1280x720+320+180')
awindow.title("Daily Puzzles")
entry=tk.Entry(awindow, font=("Comfortaa", 14), width=30)
entry.pack(pady=5)
abutton=ttk.Button(awindow, text="Retrieve the puzzle for {entry}",command=puzzle).pack()
awindow.mainloop()