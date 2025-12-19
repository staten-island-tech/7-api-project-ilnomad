import tkinter as tk
import requests
import time
import chess
import chess.pgn
from io import StringIO
class puzzles:
    def __init__(self,a,b,c,d,e,f,g):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.g=g
    def puzzle():
        response = requests.get("https://lichess.org/api/puzzle/next")
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        data = response.json()
        a=data["game"]["perf"]["name"]
        b=data["game"]["clock"]
        c=data["puzzle"]["solution"]
        d=data["puzzle"]["id"]
        e=data["puzzle"]["themes"]
        f=data["game"]["pgn"]
        g=data["puzzle"]["initialPly"]
        a_a=tk.Label(window,text=f"{c},{g}",font=("Helvetica",14))
        a_a.pack()
        puzzle.__init__(a,b,c,d,e,f,g)
        puzzle.boardprint(g)
    def movechecker():
        a=False
        b=0
        c=inputentry.get()
        for d in puzzle.c:
            while a==False:
                if c==d:
                    e=tk.Label(window,text="You successfully found the move.")
                    e.place(x=950,y=100)
                    time.sleep(5)
                    e.destroy()
                    b+=1
                    a=True
                else: 
                    f=tk.Label(window,text="You didn't find the move.")
                    f.place(x=950,y=100)
                    time.sleep(5)
                    f.destroy()
    def boardprint(self,g):
        print(self.f)
        pgn=StringIO(self.f)
        chessgame=chess.pgn.read_game(pgn)
        move_number=g
        for number, move in enumerate(chessgame.mainline_moves()):
            chess.Board.push(move)
            if number==move_number:  
                break
        fen=chess.Board.fen()
        fenlabel=tk.Label(window,text=f"{fen}")
        fenlabel.place(x=200,y=200)
window=tk.Tk()
window.geometry("1280x720+320+180")
window.title("Puzzles on LiChess")
outputtext=tk.Label(window,text="LiChess Puzzles",font=("Helvetica",14))
outputtext.pack()
button=tk.Button(window,text='Retrieve a puzzle.',command=puzzles.puzzle)
button.pack(padx=10,pady=10)
movecheckerbutton=tk.Button(window,text='Check your move.',command=puzzles.movechecker)
movecheckerbutton.place(x=1000,y=150)
inputentry=tk.Entry(window)
inputentry.place(x=750,y=200)
puzzle=puzzles("","",[],"",[],"","")
alabel=tk.Label(window,text="What's the next move in this puzzle?",font=("Helvetica",14))
alabel.place(x=650,y=150)
window.mainloop()

