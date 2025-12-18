import tkinter as tk
import requests
import time
import chess
import chess.pgn
from io import StringIO
class puzzles:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f    
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
        a_a=tk.Label(window,text=f"{c},{f}",font=("Helvetica",14))
        a_a.pack()
        puzzle.__init__(a,b,c,d,e,f)
        puzzle.boardprint()
    def movechecker():
        g=False
        h=0
        i=inputentry.get()
        for j in puzzle.__c:
            while g==False:
                if i==j:
                    k=tk.Label(window,text="You successfully found the move.")
                    k.place(x=950,y=100)
                    time.sleep(5)
                    k.destroy()
                    h+=1
                    g=True
                else: 
                    a_b=tk.Label(window,text="You didn't find the move.")
                    a_b.place(x=950,y=100)
                    time.sleep(5)
                    a_b.destroy()
    def boardprint(self):
        pgn=StringIO(puzzle.__f)
        game=chess.pgn.read_game(pgn)
        move_number = 8
        for number, move in enumerate(game.mainline_moves()):
            board.push(move)
            if number == move_number:  
                break
        fen = board.fen()
        print(fen)
        print(game)
        game=chess.Board()
        print(game)

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
puzzle=puzzles("","",[],"",[],"")
alabel=tk.Label(window,text="What's the next move in this puzzle?",font=("Helvetica",14))
alabel.place(x=650,y=150)
window.mainloop()

