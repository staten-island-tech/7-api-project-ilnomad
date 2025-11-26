import tkinter as tk
import requests

def puzzle():
    response = requests.get("https://lichess.org/api/puzzle/next")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    a=data["game"]["perf"]["name"],
    b=data["game"]["clock"],
    c=data["puzzle"]["solution"],
    d=data["game"]["pgn"]

buttonpressed=False
window=tk.Tk()
window.geometry('1280x720+320+180')
window.title("Puzzles on LiChess")
button=tk.Button(window,text=f"Retrieve a random puzzle.",command=puzzle)
button.pack(padx=10,pady=10)
outputtext=tk.Label(window,text="0,0,0",font=("Courier New",14),fg="blue",wraplength=10)
if buttonpressed==True:
    outputtext.config(text=a,font=("Courier New",14),fg="blue")
    outputtext.config(text=b,font=("Courier New",14),fg="blue")
    outputtext.config(text=c,font=("Courier New",14),fg="blue")
    outputtext.config(text=d,font=("Courier New",14),fg="blue")
window.mainloop()

