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

a1=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
a2=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
a3=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
a4=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
a5=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
a6=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
a7=tk.Button(window,text="dd",bg=("#739552"),fg=("#7d9552"),activebackground=("#739552"),activeforeground=("#739552"))
a8=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
b1=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
b2=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
b3=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
b4=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
b5=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
b6=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
b7=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
b8=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
c1=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
c2=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
c3=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
c4=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
c5=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
c6=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
c7=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
c8=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
d1=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
d2=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
d3=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
d4=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
d5=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
d6=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
d7=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
d8=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
e1=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
e2=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
e3=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
e4=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
e5=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
e6=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
e7=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
e8=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
f1=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
f2=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
f3=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
f4=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
f5=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
f6=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
f7=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
f8=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
g1=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
g2=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
g3=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
g4=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
g5=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
g6=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
g7=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
g8=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
h1=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
h2=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
h3=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
h4=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
h5=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
h6=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
h7=tk.Button(window,text="dd",bg=("#739552"),fg=("#739552"),activebackground=("#739552"),activeforeground=("#739552"))
h8=tk.Button(window,text="dd",bg=("#ebecd0"),fg=("#ebecd0"),activebackground=("#ebecd0"),activeforeground=("#ebecd0"))
a1,a2,a3,a4,a5,a6,a7,a8,b1,b2,b3,b4,b5,b6,b7,b8,c1,c2,c3,c4,c5,c6,c7,c8,d1,d2,d3,d4,d5,d6,d7,d8,e1,e2,e3,e4,e5,e6,e7,e8,f1,f2,f3,f4,f5,f6,f7,f8,g1,g2,g3,g4,g5,g6,g7,g8,h1,h2,h3,h4,h5,h6,h7,h8.pack()


window.mainloop()

#board
#select square
#pieces on board