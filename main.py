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
        
class Bauer(Figur):
    def __init__(self, farbe, num):
        self.num = num
        super().__init__(farbe)
        
        start = True
        if start == True:
            self.pos = [None,None]
            self.new_pos = [None, None]
            #startpositionen
            if self.farbe == "w":
                self.pos[1] = 6
            else:
                self.pos[1] = 1
            self.pos[0] = self.num -1
            start = False
        
        

        # Umwandlung zu anderen Figuren sobald Bauer die andere Spielseite erreicht (funktioniert nicht)
        self.umwandlung = False
        
        
        """if self.farbe == "w" and self.posY == 7:
            self.umwandlung = True
        elif self.farbe == "b" and self.posY == 0:
            self.umwandlung = True"""
    
    

    def bauer_pos_moves(self):
        #beim ersten zug 1 oder 2 nach vorne, dann nur 1
        #wenn figur diagonal [pos[0] + 1, pos[1] + 1] steht
        #wenn bauer 2 nach vorne geht (en passant)

        if self.farbe == "w" and self.pos[1] == 6:
            self.new_pos[0] = self.pos[0]
            self.new_pos[1] = [5, 4]

        elif self.farbe == "b" and self.pos[1] == 1:
            self.new_pos[0] = self.pos[0]
            self.new_pos[1] = [2, 3]

        else:
            self.new_pos[0] = self.pos[0]
            self.new_pos[1] = self.pos[1] + 1
            
            
            
class Springer(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
        self.new_pos = [None, None]
    
    def springer_startpos(self, farbe, num):
        if num == 1:
            self.posX = 1
        else:
            self.posX = 6
        if farbe == "w":
            self.posY = 0
        else:
            self.posY = 7

    def springer_pos_moves(self):
        # kann nur 2 nach vorne und 1 zur seite
        # wenn nach vorne: [pos[0] + 1 oder -1, pos[1] + 2 oder -2
        # wenn zur seite: [pos[0] + 2 oder -2, pos[1] + 1 oder -2
        self.new_pos[0], self.new_pos[1] = [self.pos[0]+1, self.pos[1]+2], [self.pos[0]-1, self.pos[1]+2]
        
        


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

    def laeufer_pos_moves(self):
        # diagonal, also new_pos[pos[0]+ i in range(bis zum ende des bretts)], pos[1] + i in range(bis zum ende des bretts)]
        pass
        
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

    def turm_pos_moves(self):
        # nur seitlich oder vertikal
        # seitlich: [pos[0] +/- i in range(bis zum ende des brett], pos[1]]
        # vertikal: [pos[0], pos[1] +/- i in range(bis zum ende des brett]
        # castling beachten
        pass
        
class Dame(Figur):
    def __init__(self, farbe):
        super().__init__(farbe)
        """self.pos = [self.posX, self.posY]
        
    def dame_startpos(self, farbe):
        self.posX = 3
        if farbe == "w":
            self.posY = 0
        else:
            self.posY = 7"""

    def dame_pos_moves(self):
        # seitlich, vertikal, diagonal
        # seitlich: [pos[0] +/- i in range(bis zum ende des brett], pos[1]]
        # vertikal: [pos[0], pos[1] +/- i in range(bis zum ende des brett]
        # diagonal, also new_pos[pos[0]+ i in range(bis zum ende des bretts)], pos[1] + i in range(bis zum ende des bretts)]
        pass

class Koenig(Figur):
    def __init__(self, farbe):
        super().__init__(farbe)
        
        self.posX = 0
        self.posY = 0
        self.pos = [self.posX, self.posY]
    def koenig_startpos(self, farbe):
        self.posX = 4
        if farbe == "w":
            self.posY = 0
        else:
            self.posY = 7

    def koenig_pos_moves(self):
        # 1 seitlich und diagonal
        # [pos[0] +/- 1, pos[1] +/- 1
        pass

global chess_board
chess_board = [[0 for i in range(8)] for j in range(8)]

global wking, wqueen, wrook, wbishop, wknight, wpawn, bking, bqueen, brook, bbishop, bknight, bpawn

color = {0: "w", 1: "b"}


for i in range(1):
    king = {
        "name": color[i]+ "könig",
        "figur": Koenig(color[i])
}
    dame = {
        "name":color[i] + "dame",
        "figur": Dame(color[i])
    }



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
chess_board[7][4] = king["name"]
chess_board[7][5] = wbishop
chess_board[7][6] = wknight
chess_board[7][7] = wrook
print(chess_board)


# position von figur herausfinden
"""for i in range(8): 
    for j in range(8):
        if chess_board[j][i] == wrook:
            print(i,j)"""

def buttoncheck(event):
    print("event:", event)
    print("event.widget:", event.widget)
    
    # Row und column werte bekommen
    row = event.widget.grid_info()["row"]
    column = event.widget.grid_info()["column"]
    print(row, column)
    
    

    
    

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
    
    
    x = Bauer("w",1)
    x.pos = [5,4]
    x.bauer_pos_moves()
    addImg(frame_list[x.new_pos[0]][x.new_pos[1]], img["bp"])
    print(x.new_pos)
    
    startaufstellung()
    
    root.mainloop()


createWin()
