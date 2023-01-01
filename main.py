from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
# Dictionary to store the images for each chess piece
img = {}

# Letters to use for labeling the chess board
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Create the root window
root = tk.Tk()
board = tk.Frame(root, bg="white", width=800, height=800)
root.geometry("800x800")
root.wm_attributes("-transparentcolor")




# Load the images for each chess piece and resize them
photo = Image.open("pieces/blackpawn.png")
bpawn_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/whitepawn.png")
wpawn_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/blackrook.png")
brook_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/whiterook.png")
wrook_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/blackknight.png")
bknight_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/whiteknight.png")
wknight_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/blackbishop.png")
bbishop_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/whitebishop.png")
wbishop_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/blackqueen.png")
bqueen_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/whitequeen.png")
wqeen_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/blackking.png")
bking_img = ImageTk.PhotoImage(photo.resize((40, 40)))
photo = Image.open("pieces/whiteking.png")
wking_img = ImageTk.PhotoImage(photo.resize((40, 40)))


img["bp"] = bpawn_img
img["wp"] = wpawn_img
img["br"] = brook_img
img["wr"] = wrook_img
img["bkn"] = bknight_img
img["wkn"] = wknight_img
img["bb"] = bbishop_img
img["wb"] = wbishop_img
img["bq"] = bqueen_img
img["wq"] = wqeen_img
img["bk"] = bking_img
img["wk"] = wking_img


# Klassen (https://www.w3schools.com/python/python_classes.asp; https://www.w3schools.com/python/python_inheritance.asp)
class Figur:
    def __init__(self, farbe):
        self.farbe = farbe
        self.posX = 0
        self.posY = 0
        
class Bauer(Figur):
    def __init__(self, farbe, num):
        self.num = num
        super().__init__(farbe)

        self.pos = [self.posX, self.posY]
        
        # Umwandlung zu anderen Figuren sobald Bauer die andere Spielseite erreicht (funktioniert nicht)
        self.umwandlung = False
        
        
        if self.farbe == "w" and self.posY == 7:
            self.umwandlung = True
        elif self.farbe == "b" and self.posY == 0:
            self.umwandlung = True
    def bauer_startpos(self):
        self.bauer_startposX()
        self.bauer_startposY()
    def bauer_startposX(self):
        # Startpositionen der verschiedenen Bauern 
        self.posX = self.num
        return self.posX
    def bauer_startposY(self):
        if self.farbe == "w":
            self.posY = 1
        else:
            self.posY = 6
        return self.posY
        
class Springer(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
    
    def springer_startpos(self, farbe, num):
        if num == 1:
            self.posX = 1
        else:
            self.posX = 6
        if farbe == "w":
            self.posY = 0
        else:
            self.posY = 7
        
class Laeufer(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
        
    def laeufer_startpos(self, farbe, num):
        if num == 1:
            self.posX = 2
        else:
            self.posX = 5
        if farbe == "w":
            self.posY = 0
        else:
            self.posY = 7
        
class Turm(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
        
    def turm_startpos(self, farbe, num):
        if num == 1:
            self.posX = 0
        else:
            self.posX = 7
        if farbe == "w":
            self.posY = 0
        else:
            self.posY = 7
        
class Dame(Figur):
    def __init__(self, farbe):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
        
    def dame_startpos(self, farbe):
        self.posX = 3
        if farbe == "w":
            self.posY = 0
        else:
            self.posY = 7
            
class Koenig(Figur):
    def __init__(self, farbe):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
        
    def koenig_startpos(self, farbe):
        self.posX = 4
        if farbe == "w":
            self.posY = 0
        else:
            self.posY = 7









global chess_board
chess_board = [[0 for i in range(8)] for j in range(8)]

global wking, wqueen, wrook, wbishop, wknight, wpawn, bking, bqueen, brook, bbishop, bknight, bpawn
wking = "wkönig"
wqueen = "wdame"
wrook = "wturm"
wbishop = "wläufer"
wknight = "wspringer"
wpawn = "wbauer"

bking = "bkönig"
bqueen = "bdame"
brook = "bturm"
bbishop = "bläufer"
bknight = "bspringer"
bpawn = "bbauer"

chess_board[0][0] = brook
chess_board[0][1] = bknight
chess_board[0][2] = bbishop
chess_board[0][3] = bqueen
chess_board[0][4] = bking
chess_board[0][5] = bbishop
chess_board[0][6] = bknight
chess_board[0][7] = brook
for i in range(8):
    chess_board[1][i] = bpawn
    chess_board[6][i] = wpawn
chess_board[7][0] = wrook
chess_board[7][1] = wknight
chess_board[7][2] = wbishop
chess_board[7][3] = wqueen
chess_board[7][4] = wking
chess_board[7][5] = wbishop
chess_board[7][6] = wknight
chess_board[7][7] = wrook


# position von figur herausfinden
"""for i in range(8): 
    for j in range(8):
        if chess_board[j][i] == wrook:
            print(i,j)"""

def buttoncheck(event):
    print("event:", event)
    print("event.widget:", event.widget)

def createGrid():

    
    # Visuelle darstellung des schachbretts
    global frame_list
    frame_list = [[None for i in range(8)] for j in range(8)]
    for i in range(8):  # erstellt die felder als frames für das schachbrettmuster
        for j in range(8):
            # Set the background color based on the position
            color = "white" if (i + j) % 2 == 0 else "gray"
            frame = tk.Frame(bg=color, width=100, height=100)
            frame.grid(row=i, column=j, sticky="nsew")
            frame.bind("<Button-1>", buttoncheck)
            frame_list[j][i] = frame # https://stackoverflow.com/questions/71576597/how-to-use-tkinter-config-on-a-grid-of-frames
    
    
    
def addImg(list, img):   # Fügt bilder als labels in die felder ein
    for i in range(8):
        for j in range(8):
            if frame_list[j][i] == list:
                piece = Label(frame_list[j][i], image=img, background=frame_list[j][i]["background"], width=90, height=96)
                piece.pack(expand=TRUE)
                piece.bind("<Button-1>", buttoncheck)

    
    
    
def startaufstellung():
        for i in range(8):
            for j in range(8):
                match chess_board[i][j]:
                    case "bbauer":
                        addImg(frame_list[j][i], img["bp"])
                    case "wbauer":
                        addImg(frame_list[j][i], img["wp"])
                    case "wturm":
                        addImg(frame_list[j][i], img["wr"])
                    case "bturm":
                        addImg(frame_list[j][i], img["br"])
                    case "wspringer":
                        addImg(frame_list[j][i], img["wkn"])
                    case "bspringer":
                        addImg(frame_list[j][i], img["bkn"])
                    case "wläufer":
                        addImg(frame_list[j][i], img["wb"])
                    case "bläufer":
                        addImg(frame_list[j][i], img["bb"])
                    case "wkönig":
                        addImg(frame_list[j][i], img["wk"])
                    case "bkönig":
                        addImg(frame_list[j][i], img["bk"])
                    case "wdame":
                        addImg(frame_list[j][i], img["wq"])
                    case "bdame":
                        addImg(frame_list[j][i], img["bq"])

def createWin(): # Fenster erstellen (https://www.pythonguis.com/tutorials/create-gui-tkinter/)
    root.title("Schach")
    
    createGrid()
    
    """bruh = Label(image=bpawn)
        bruh.grid(row=1,column=1)"""
    """gray1.configure(image=bpawn)
    
        gray1.bind("<Button-1>", lambda e: buttoncheck())"""
    
    
    
    
    startaufstellung()
    
    root.mainloop()
# kein bock mehr auf das grid mit knöpfen oder anderen scheiß, 

createWin()
