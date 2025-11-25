import tkinter as tk
from tkinter import ttk
import requests

def puzzle():
    response = requests.get("https://lichess.org/api/puzzle/daily")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    print("air")
    return{
        "Gamemode": data["game"]["perf"]["name"],
        "Clock": data["game"]["clock"],
        "Solution": data["puzzle"]["solution"],
        "PGN": data["game"]["pgn"]
    }
def printpuzzle():
    print(puzzle())

window=tk.Tk()
window.geometry('1280x720+320+180')
window.title("Daily Puzzles on LiChess")
entry=tk.Entry(window, font=("Comfortaa", 14), width=30)
entry.pack(pady=5)
date=entry.get
button=tk.Button(window,text=f"Retrieve the daily puzzle for any date available.",command=printpuzzle)
button.pack(padx=10,pady=10)
window.mainloop()