from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

img = {}

# Fenster erstellen
root = tk.Tk()
board = tk.Frame(root, bg="white", width=800, height=800)
root.geometry("1000x800")
root.wm_attributes("-transparentcolor")


# Bilder von Schachfiguren öffnen und laden
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

schachw = False
schachb = False
schachmattw = False
schachmattb = False

# Klassen (https://www.w3schools.com/python/python_classes.asp; https://www.w3schools.com/python/python_inheritance.asp)
class Figur:
    def __init__(self, farbe):
        self.farbe = farbe


class Bauer(Figur):
    def __init__(self, farbe, num):
        self.num = num

        super().__init__(farbe)
        if self.farbe == "w":
            self.pos = [6, self.num - 1]

        if self.farbe == "b":
            self.pos = [1, self.num - 1]

        self.art = "bauer"

        # Umwandlung zu anderen Figuren sobald Bauer die andere Spielseite erreicht (funktioniert nicht)
        self.umwandlung = False

        """if self.farbe == "w" and self.posY == 7:
            self.umwandlung = True
        elif self.farbe == "b" and self.posY == 0:
            self.umwandlung = True"""
    # Mögliche Züge für Bauer
    def pos_moves(self):
        # beim ersten zug 1 oder 2 nach vorne, dann nur 1
        # wenn figur diagonal [pos[0] + 1, pos[1] + 1] steht
        # wenn bauer 2 nach vorne geht (en passant)
        self.new_pos = []

        if self.farbe == "w" and self.pos[0] == 6 and chess_board[self.pos[0]-1][self.pos[1]] == 0:
            self.new_pos.append([5, self.pos[1]])
            self.new_pos.append([4, self.pos[1]])


        if self.farbe == "b" and self.pos[0] == 1 and chess_board[self.pos[0]+1][self.pos[1]] == 0:
            self.new_pos.append([3, self.pos[1]])
            self.new_pos.append([2, self.pos[1]])

        if self.farbe == "w" and self.pos[0] != 6 and chess_board[self.pos[0]-1][self.pos[1]] == 0:

            self.new_pos.append([self.pos[0] - 1, self.pos[1]])

        if self.farbe == "b" and self.pos[0] != 1 and chess_board[self.pos[0]+1][self.pos[1]] == 0:

            self.new_pos.append([self.pos[0] + 1, self.pos[1]])
        #Falls bei weißen eine figur oben links steht
        if self.pos[1] != 0 and self.farbe == "w" and chess_board[self.pos[0]-1][self.pos[1]-1] != 0:
            self.new_pos.append([self.pos[0] - 1, self.pos[1]-1])
        # Falls bei weißen eine figur oben rechts steht
        if self.pos[1] != 7 and self.farbe == "w" and chess_board[self.pos[0]-1][self.pos[1]+1] != 0 :
            self.new_pos.append([self.pos[0] - 1, self.pos[1]+1])
        #Falls bei schwarzen eine figur unten links steht
        if self.pos[1] != 0 and self.farbe == "b" and chess_board[self.pos[0]+1][self.pos[1]-1] != 0:
            self.new_pos.append([self.pos[0] + 1, self.pos[1]-1])
        #Falls bei schwarzen eine figur unten rechts steht
        if self.pos[1] != 7 and self.farbe == "b" and chess_board[self.pos[0]+1][self.pos[1]+1] != 0:
            self.new_pos.append([self.pos[0] + 1, self.pos[1]+1])
            
        global schachw
        global schachb
        for i in range(len(self.new_pos)):
            if self.farbe == "w" and self.new_pos[i] == king["figurb"].pos:
                schachb = True
            elif self.farbe == "b" and self.new_pos[i] == king["figurw"].pos:
                schachw = True

class Springer(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.num = num
        if self.num == 1 and self.farbe == "w":
            self.pos = [7, 1]
        elif self.num == 2 and self.farbe == "w":
            self.pos = [7, 6]
        elif self.num == 1 and self.farbe == "b":
            self.pos = [0, 1]
        elif self.num == 2 and self.farbe == "b":
            self.pos = [0, 6]
        self.art = "springer"

    # Mögliche Züge für Springer
    def pos_moves(self):
        # kann nur 2 nach vorne und 1 zur seite
        # wenn nach vorne: [pos[0] + 1 oder -1, pos[1] + 2 oder -2
        # wenn zur seite: [pos[0] + 2 oder -2, pos[1] + 1 oder -2
        global schachw
        global schachb
        
        self.new_pos = []

        self.new_pos.append([self.pos[0] + 2, self.pos[1] + 1])
        self.new_pos.append([self.pos[0] + 2, self.pos[1] - 1])
        self.new_pos.append([self.pos[0] - 2, self.pos[1] + 1])
        self.new_pos.append([self.pos[0] - 2, self.pos[1] - 1])
        self.new_pos.append([self.pos[0] + 1, self.pos[1] + 2])
        self.new_pos.append([self.pos[0] - 1, self.pos[1] + 2])
        self.new_pos.append([self.pos[0] + 1, self.pos[1] - 2])
        self.new_pos.append([self.pos[0] - 1, self.pos[1] - 2])



        for i in range(len(self.new_pos)):
            if self.new_pos[i][0] >= 8 or self.new_pos[i][1] >= 8 or self.new_pos[i][0] < 0 or self.new_pos[i][1] < 0:
                self.new_pos[i][0] = None
                self.new_pos[i][1] = None
            if self.farbe == "w" and self.new_pos[i] == king["figurb"].pos:
                schachb = True
            elif self.farbe == "b" and self.new_pos[i] == king["figurw"].pos:
                schachw = True
        
        

class Laeufer(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.num = num

        if self.num == 1 and self.farbe == "w":
            self.pos = [7, 2]
        elif self.num == 2 and self.farbe == "w":
            self.pos = [7, 5]
        elif self.num == 1 and self.farbe == "b":
            self.pos = [0, 2]
        else:
            self.pos = [0, 5]
        self.art = "läufer"

    # Mögliche Züge für Läufer
    def pos_moves(self):
        # diagonal, also new_pos[pos[0]+ i in range(bis zum ende des bretts)], pos[1] + i in range(bis zum ende des bretts)]
        self.new_pos = []
        self.hochlinks = []
        self.hochrechts = []
        self.untenlinks = []
        self.untenrechts = []
        self.schachlinie = []
        for i in range(1, 8):
            if self.pos[0] + i >= 0 and self.pos[1] + i >= 0 and self.pos[0] + i < 8 and self.pos[1] + i < 8:
                self.new_pos.append([self.pos[0] + i, self.pos[1] + i])
                self.untenrechts.append([self.pos[0] + i, self.pos[1] + i])

            if self.pos[0] + i >= 0 and self.pos[1] - i >= 0 and self.pos[0] + i < 8 and self.pos[1] - i < 8:
                self.new_pos.append([self.pos[0] + i, self.pos[1] - i])
                self.untenlinks.append([self.pos[0] + i, self.pos[1] - i])

            if self.pos[0] - i >= 0 and self.pos[1] - i >= 0 and self.pos[0] - i < 8 and self.pos[1] - i < 8:
                self.new_pos.append([self.pos[0] - i, self.pos[1] - i])
                self.hochlinks.append([self.pos[0] - i, self.pos[1] - i])

            if self.pos[0] - i >= 0 and self.pos[1] + i >= 0 and self.pos[0] - i < 8 and self.pos[1] + i < 8:
                self.new_pos.append([self.pos[0] - i, self.pos[1] + i])
                self.hochrechts.append([self.pos[0] - i, self.pos[1] + i])
        
        # Zum überprüfen ob andere Figuren im Weg sind
        for i in range(1,8):
            if self.pos[0] + i >= 0 and self.pos[1] + i >= 0 and self.pos[0] + i < 8 and self.pos[1] + i < 8 and chess_board[self.pos[0]+i][self.pos[1]+i]:
                for j in range(i,8):
                    if [self.pos[0]+j+1, self.pos[1]+j+1] in self.new_pos:
                        self.new_pos.remove([self.pos[0]+j+1, self.pos[1]+j+1])
            
            if self.pos[0] + i >= 0 and self.pos[1] - i >= 0 and self.pos[0] + i < 8 and self.pos[1] - i < 8 and chess_board[self.pos[0]+i][self.pos[1]-i]:
                for j in range(i,8):
                    if [self.pos[0]+j+1, self.pos[1]-j-1] in self.new_pos:
                        self.new_pos.remove([self.pos[0]+j+1, self.pos[1]-j-1])
                        
            if self.pos[0] - i >= 0 and self.pos[1] - i >= 0 and self.pos[0] - i < 8 and self.pos[1] - i < 8 and chess_board[self.pos[0]-i][self.pos[1]-i]:
                for j in range(i,8):
                    if [self.pos[0]-j-1, self.pos[1]-j-1] in self.new_pos:
                        self.new_pos.remove([self.pos[0]-j-1, self.pos[1]-j-1])
                        
            if self.pos[0] - i >= 0 and self.pos[1] + i >= 0 and self.pos[0] - i < 8 and self.pos[1] + i < 8 and chess_board[self.pos[0]-i][self.pos[1]+i]:
                for j in range(i,8):
                    if [self.pos[0]-j-1, self.pos[1]+j+1] in self.new_pos:
                        self.new_pos.remove([self.pos[0]-j-1, self.pos[1]+j+1])
                    
        global schachw
        global schachb
        for i in range(len(self.new_pos)):
            hl = self.hochlinks.count(king["figurb"].pos)
            hr = self.hochrechts.count(king["figurb"].pos)
            ul = self.untenlinks.count(king["figurb"].pos)
            ur = self.untenrechts.count(king["figurb"].pos)
            if hl <= 1:
                self.schachlinie = self.hochlinks
            elif hr <= 1:
                self.schachlinie = self.hochrechts
            elif ul <= 1:
                self.schachlinie = self.untenlinks
            elif ur <= 1:
                self.schachlinie = self.untenrechts
            if self.farbe == "w" and self.new_pos[i] == king["figurb"].pos:
                schachb = True
                
            elif self.farbe == "b" and self.new_pos[i] == king["figurw"].pos:
                schachw = True         
        
        
        


class Turm(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)

        self.num = num

        if self.num == 1 and self.farbe == "w":
            self.pos = [7, 0]
        elif self.num == 2 and self.farbe == "w":
            self.pos = [7, 7]
        elif self.num == 1 and farbe == "b":
            self.pos = [0, 0]
        else:
            self.pos = [0, 7]
        self.art = "turm"
        
    # Mögliche Züge für Turm
    def pos_moves(self):
        # nur seitlich oder vertikal
        # seitlich: [pos[0] +/- i in range(bis zum ende des brett], pos[1]]
        # vertikal: [pos[0], pos[1] +/- i in range(bis zum ende des brett]
        # castling beachten
        self.new_pos = []
        self.hoch = []
        self.rechts = []
        self.links = []
        self.unten = []
        self.schachlinie = []
        for i in range(1, 8):
            if self.pos[0] + i < 8 and self.pos[0] + i >= 0:
                self.new_pos.append([self.pos[0] + i, self.pos[1]])
                self.unten.append([self.pos[0] + i, self.pos[1]])

            if self.pos[0] - i < 8 and self.pos[0] - i >= 0:
                self.new_pos.append([self.pos[0] - i, self.pos[1]])
                self.hoch.append([self.pos[0] - i, self.pos[1]])

            if self.pos[1] + i < 8 and self.pos[1] + i >= 0:
                self.new_pos.append([self.pos[0], self.pos[1] + i])
                self.rechts.append([self.pos[0], self.pos[1] + i])

            if self.pos[1] - i < 8 and self.pos[1] - i >= 0:
                self.new_pos.append([self.pos[0], self.pos[1] - i])
                self.links.append([self.pos[0], self.pos[1] - i])


        for i in range(1,8):
            if self.pos[0] + i < 8 and self.pos[0] + i >= 0 and chess_board[self.pos[0]+i][self.pos[1]]:
                 for j in range(i,8):
                     if [self.pos[0]+j+1, self.pos[1]] in self.new_pos:
                         self.new_pos.remove([self.pos[0]+j+1, self.pos[1]])                
                         
            if self.pos[0] - i < 8 and self.pos[0] - i >= 0 and chess_board[self.pos[0]-i][self.pos[1]]:
                 for j in range(i,8):
                     if [self.pos[0]-j-1, self.pos[1]] in self.new_pos:
                         self.new_pos.remove([self.pos[0]-j-1, self.pos[1]])

            if self.pos[1] + i < 8 and self.pos[1] + i >= 0 and chess_board[self.pos[0]][self.pos[1]+i]:
                 for j in range(i,8):
                     if [self.pos[0], self.pos[1]+j+1] in self.new_pos:
                         self.new_pos.remove([self.pos[0], self.pos[1]+j+1])
        
            if self.pos[1] - i < 8 and self.pos[1] - i >= 0 and chess_board[self.pos[0]][self.pos[1]-i]:
                 for j in range(i,8):
                     if [self.pos[0], self.pos[1]-j-1] in self.new_pos:
                         self.new_pos.remove([self.pos[0], self.pos[1]-j-1])
        global schachw
        global schachb
        
        for i in range(len(self.new_pos)):
            h = self.hoch.count(king["figurb"].pos)
            r = self.rechts.count(king["figurb"].pos)
            l = self.links.count(king["figurb"].pos)
            u = self.unten.count(king["figurb"].pos)
            if h <= 1:
                self.schachlinie = self.hoch
            elif r <= 1:
                self.schachlinie = self.rechts
            elif l <= 1:
                self.schachlinie = self.links
            elif u <= 1:
                self.schachlinie = self.unten
            if self.farbe == "w" and self.new_pos[i] == king["figurb"].pos:
                schachb = True
            elif self.farbe == "b" and self.new_pos[i] == king["figurw"].pos:
                schachw = True
                
class Dame(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.num = num
        if self.farbe == "w":
            self.pos = [7, 3]
        else:
            self.pos = [0, 3]
        self.art = "dame"
        
    # Mögliche Züge für Dame
    def pos_moves(self):
        # seitlich, vertikal, diagonal
        # seitlich: [pos[0] +/- i in range(bis zum ende des brett], pos[1]]
        # vertikal: [pos[0], pos[1] +/- i in range(bis zum ende des brett]
        # diagonal, also new_pos[pos[0]+ i in range(bis zum ende des bretts)], pos[1] + i in range(bis zum ende des bretts)]
        self.new_pos = []
        self.hochlinks = []
        self.hochrechts = []
        self.untenlinks = []
        self.untenrechts = []
        self.hoch = []
        self.rechts = []
        self.links = []
        self.unten = []
        global schachw
        global schachb
        for i in range(1, 8):
            if self.pos[0] + i >= 0 and self.pos[1] + i >= 0 and self.pos[0] + i < 8 and self.pos[1] + i < 8:
                self.new_pos.append([self.pos[0] + i, self.pos[1] + i])
                self.untenrechts.append([self.pos[0] + i, self.pos[1] + i])

            if self.pos[0] + i >= 0 and self.pos[1] - i >= 0 and self.pos[0] + i < 8 and self.pos[1] - i < 8:
                self.new_pos.append([self.pos[0] + i, self.pos[1] - i])
                self.untenlinks.append([self.pos[0] + i, self.pos[1] - i])

            if self.pos[0] - i >= 0 and self.pos[1] - i >= 0 and self.pos[0] - i < 8 and self.pos[1] - i < 8:
                self.new_pos.append([self.pos[0] - i, self.pos[1] - i])
                self.hochlinks.append([self.pos[0] - i, self.pos[1] - i])

            if self.pos[0] - i >= 0 and self.pos[1] + i >= 0 and self.pos[0] - i < 8 and self.pos[1] + i < 8:
                self.new_pos.append([self.pos[0] - i, self.pos[1] + i])
                self.hochrechts.append([self.pos[0] - i, self.pos[1] + i])

            if self.pos[0] + i < 8 and self.pos[0] + i >= 0:
                self.new_pos.append([self.pos[0] + i, self.pos[1]])
                self.unten.append([self.pos[0] + i, self.pos[1]])

            if self.pos[0] - i < 8 and self.pos[0] - i >= 0:
                self.new_pos.append([self.pos[0] - i, self.pos[1]])
                self.hoch.append([self.pos[0] - i, self.pos[1]])

            if self.pos[1] + i < 8 and self.pos[1] + i >= 0:
                self.new_pos.append([self.pos[0], self.pos[1] + i])
                self.rechts.append([self.pos[0], self.pos[1] + i])

            if self.pos[1] - i < 8 and self.pos[1] - i >= 0:
                self.new_pos.append([self.pos[0], self.pos[1] - i])
                self.links.append([self.pos[0], self.pos[1] - i])
            else:
                pass
            
        for i in range(1,8):
            if self.pos[0] + i >= 0 and self.pos[1] + i >= 0 and self.pos[0] + i < 8 and self.pos[1] + i < 8 and chess_board[self.pos[0]+i][self.pos[1]+i]:
                for j in range(i,8):
                    if [self.pos[0]+j+1, self.pos[1]+j+1] in self.new_pos:
                        self.new_pos.remove([self.pos[0]+j+1, self.pos[1]+j+1])
            
            if self.pos[0] + i >= 0 and self.pos[1] - i >= 0 and self.pos[0] + i < 8 and self.pos[1] - i < 8 and chess_board[self.pos[0]+i][self.pos[1]-i]:
                for j in range(i,8):
                    if [self.pos[0]+j+1, self.pos[1]-j-1] in self.new_pos:
                        self.new_pos.remove([self.pos[0]+j+1, self.pos[1]-j-1])
                        
            if self.pos[0] - i >= 0 and self.pos[1] - i >= 0 and self.pos[0] - i < 8 and self.pos[1] - i < 8 and chess_board[self.pos[0]-i][self.pos[1]-i]:
                for j in range(i,8):
                    if [self.pos[0]-j-1, self.pos[1]-j-1] in self.new_pos:
                        self.new_pos.remove([self.pos[0]-j-1, self.pos[1]-j-1])
                        
            if self.pos[0] - i >= 0 and self.pos[1] + i >= 0 and self.pos[0] - i < 8 and self.pos[1] + i < 8 and chess_board[self.pos[0]-i][self.pos[1]+i]:
                for j in range(i,8):
                    if [self.pos[0]-j-1, self.pos[1]+j+1] in self.new_pos:
                        self.new_pos.remove([self.pos[0]-j-1, self.pos[1]+j+1])

            if self.pos[0] + i < 8 and self.pos[0] + i >= 0 and chess_board[self.pos[0]+i][self.pos[1]]:
                 for j in range(i,8):
                     if [self.pos[0]+j+1, self.pos[1]] in self.new_pos:
                         self.new_pos.remove([self.pos[0]+j+1, self.pos[1]])                
                         
            if self.pos[0] - i < 8 and self.pos[0] - i >= 0 and chess_board[self.pos[0]-i][self.pos[1]]:
                 for j in range(i,8):
                     if [self.pos[0]-j-1, self.pos[1]] in self.new_pos:
                         self.new_pos.remove([self.pos[0]-j-1, self.pos[1]])

            if self.pos[1] + i < 8 and self.pos[1] + i >= 0 and chess_board[self.pos[0]][self.pos[1]+i]:
                 for j in range(i,8):
                     if [self.pos[0], self.pos[1]+j+1] in self.new_pos:
                         self.new_pos.remove([self.pos[0], self.pos[1]+j+1])
        
            if self.pos[1] - i < 8 and self.pos[1] - i >= 0 and chess_board[self.pos[0]][self.pos[1]-i]:
                 for j in range(i,8):
                     if [self.pos[0], self.pos[1]-j-1] in self.new_pos:
                         self.new_pos.remove([self.pos[0], self.pos[1]-j-1])
                         
        for i in range(len(self.new_pos)):
            hl = self.hochlinks.count(king["figurb"].pos)
            hr = self.hochrechts.count(king["figurb"].pos)
            ul = self.untenlinks.count(king["figurb"].pos)
            ur = self.untenrechts.count(king["figurb"].pos)
            h = self.hoch.count(king["figurb"].pos)
            r = self.rechts.count(king["figurb"].pos)
            l = self.links.count(king["figurb"].pos)
            u = self.unten.count(king["figurb"].pos)
            if hl <= 1:
                self.schachlinie = self.hochlinks
            elif hr <= 1:
                self.schachlinie = self.hochrechts
            elif ul <= 1:
                self.schachlinie = self.untenlinks
            elif ur <= 1:
                self.schachlinie = self.untenrechts
            elif h <= 1:
                self.schachlinie = self.hoch
            elif r <= 1:
                self.schachlinie = self.rechts
            elif l <= 1:
                self.schachlinie = self.links
            elif u <= 1:
                self.schachlinie = self.unten
            if self.farbe == "w" and self.new_pos[i] == king["figurb"].pos:
                schachb = True
            elif self.farbe == "b" and self.new_pos[i] == king["figurw"].pos:
                schachw = True
            
                
class Koenig(Figur):
    def __init__(self, farbe):
        super().__init__(farbe)
        if self.farbe == "w":
            self.pos = [7, 4]
        else:
            self.pos = [0, 4]
        self.art = "könig"
        
    # Mögliche Züge für 
    def pos_moves(self):
        # 1 seitlich und diagonal
        # [pos[0] +/- 1, pos[1] +/- 1
        self.new_pos = []
        self.new_pos.append([self.pos[0] + 1, self.pos[1] + 1])
        self.new_pos.append([self.pos[0], self.pos[1] + 1])
        self.new_pos.append([self.pos[0] - 1, self.pos[1] + 1])
        self.new_pos.append([self.pos[0] + 1, self.pos[1]])
        self.new_pos.append([self.pos[0] + 1, self.pos[1] - 1])
        self.new_pos.append([self.pos[0], self.pos[1] - 1])
        self.new_pos.append([self.pos[0] - 1, self.pos[1] - 1])
        self.new_pos.append([self.pos[0] - 1, self.pos[1]])

        for i in range(len(self.new_pos)):
            if self.new_pos[i][0] >= 8 or self.new_pos[i][1] >= 8 or self.new_pos[i][0] < 0 or self.new_pos[i][1] < 0:
                self.new_pos[i][0] = None
                self.new_pos[i][1] = None



global chess_board
chess_board = [[0 for i in range(8)] for j in range(8)]
global piece_board
piece_board = [[0 for i in range(8)] for j in range(8)]

# Dictionaries mit allen Figuren

king = {
    "namew": "wkönig",
    "nameb": "bkönig",
    "figurw": Koenig("w"),
    "figurb": Koenig("b")
}
queen = {
    "namew": "wdame",
    "nameb": "bdame",
    "figurw1": Dame("w", 1),
    "figurw2": Dame("w", 2),
    "figurw3": Dame("w", 3),
    "figurw4": Dame("w", 4),
    "figurw5": Dame("w", 5),
    "figurw6": Dame("w", 6),
    "figurw7": Dame("w", 7),
    "figurw8": Dame("w", 8),
    "figurw9": Dame("w", 9),
    "figurw10": Dame("w", 10),
    "figurb1": Dame("b", 1),
    "figurb2": Dame("b", 2),
    "figurb3": Dame("b", 3),
    "figurb4": Dame("b", 4),
    "figurb5": Dame("b", 5),
    "figurb6": Dame("b", 6),
    "figurb7": Dame("b", 7),
    "figurb8": Dame("b", 8),
    "figurb9": Dame("b", 9),
    "figurb10": Dame("b", 10)
}

rook = {
    "namew": "wturm",
    "nameb": "bturm",
    "figurw1": Turm("w", 1),
    "figurw2": Turm("w", 2),
    "figurb1": Turm("b", 1),
    "figurb2": Turm("b", 2),
}

bishop = {
    "namew": "wläufer",
    "nameb": "bläufer",
    "figurw1": Laeufer("w", 1),
    "figurw2": Laeufer("w", 2),
    "figurb1": Laeufer("b", 1),
    "figurb2": Laeufer("b", 2)
}

knight = {
    "namew": "wspringer",
    "nameb": "bspringer",
    "figurw1": Springer("w", 1),
    "figurw2": Springer("w", 2),
    "figurb1": Springer("b", 1),
    "figurb2": Springer("b", 2)
}

pawn = {
    "namew": "wbauer",
    "nameb": "bbauer",
    "figurw1": Bauer("w", 1),
    "figurw2": Bauer("w", 2),
    "figurw3": Bauer("w", 3),
    "figurw4": Bauer("w", 4),
    "figurw5": Bauer("w", 5),
    "figurw6": Bauer("w", 6),
    "figurw7": Bauer("w", 7),
    "figurw8": Bauer("w", 8),
    "figurb1": Bauer("b", 1),
    "figurb2": Bauer("b", 2),
    "figurb3": Bauer("b", 3),
    "figurb4": Bauer("b", 4),
    "figurb5": Bauer("b", 5),
    "figurb6": Bauer("b", 6),
    "figurb7": Bauer("b", 7),
    "figurb8": Bauer("b", 8)
}

# 2D darstellung mit Listen der Figuren
chess_board[rook["figurb1"].pos[0]][rook["figurb1"].pos[1]] = rook["nameb"]
chess_board[knight["figurb1"].pos[0]][knight["figurb1"].pos[1]] = knight["nameb"]
chess_board[bishop["figurb1"].pos[0]][bishop["figurb1"].pos[1]] = bishop["nameb"]
chess_board[queen["figurb1"].pos[0]][queen["figurb1"].pos[1]] = queen["nameb"]
chess_board[king["figurb"].pos[0]][king["figurb"].pos[1]] = king["nameb"]
chess_board[bishop["figurb2"].pos[0]][bishop["figurb2"].pos[1]] = bishop["nameb"]
chess_board[knight["figurb2"].pos[0]][knight["figurb2"].pos[1]] = knight["nameb"]
chess_board[rook["figurb2"].pos[0]][rook["figurb2"].pos[1]] = rook["nameb"]
for i in range(1, 9):
    chess_board[pawn["figurb%s" % (i)].pos[0]][pawn["figurb%s" % (i)].pos[1]] = pawn["nameb"]
    chess_board[pawn["figurw%s" % (i)].pos[0]][pawn["figurw%s" % (i)].pos[1]] = pawn["namew"]
chess_board[rook["figurw1"].pos[0]][rook["figurw1"].pos[1]] = rook["namew"]
chess_board[knight["figurw1"].pos[0]][knight["figurw1"].pos[1]] = knight["namew"]
chess_board[bishop["figurw1"].pos[0]][bishop["figurw1"].pos[1]] = bishop["namew"]
chess_board[queen["figurw1"].pos[0]][queen["figurw1"].pos[1]] = queen["namew"]
chess_board[king["figurw"].pos[0]][king["figurw"].pos[1]] = king["namew"]
chess_board[bishop["figurw2"].pos[0]][bishop["figurw2"].pos[1]] = bishop["namew"]
chess_board[knight["figurw2"].pos[0]][knight["figurw2"].pos[1]] = knight["namew"]
chess_board[rook["figurw2"].pos[0]][rook["figurw2"].pos[1]] = rook["namew"]

#####


piece_board[rook["figurb1"].pos[0]][rook["figurb1"].pos[1]] = rook["figurb1"]
piece_board[knight["figurb1"].pos[0]][knight["figurb1"].pos[1]] = knight["figurb1"]
piece_board[bishop["figurb1"].pos[0]][bishop["figurb1"].pos[1]] = bishop["figurb1"]
piece_board[queen["figurb1"].pos[0]][queen["figurb1"].pos[1]] = queen["figurb1"]
piece_board[king["figurb"].pos[0]][king["figurb"].pos[1]] = king["figurb"]
piece_board[bishop["figurb2"].pos[0]][bishop["figurb2"].pos[1]] = bishop["figurb2"]
piece_board[knight["figurb2"].pos[0]][knight["figurb2"].pos[1]] = knight["figurb2"]
piece_board[rook["figurb2"].pos[0]][rook["figurb2"].pos[1]] = rook["figurb2"]
for i in range(1, 9):
    piece_board[pawn["figurb%s" % (i)].pos[0]][pawn["figurb%s" % (i)].pos[1]] = pawn["figurb%s" % (i)]
    piece_board[pawn["figurw%s" % (i)].pos[0]][pawn["figurw%s" % (i)].pos[1]] = pawn["figurw%s" % (i)]
piece_board[rook["figurw1"].pos[0]][rook["figurw1"].pos[1]] = rook["figurw1"]
piece_board[knight["figurw1"].pos[0]][knight["figurw1"].pos[1]] = knight["figurw1"]
piece_board[bishop["figurw1"].pos[0]][bishop["figurw1"].pos[1]] = bishop["figurw1"]
piece_board[queen["figurw1"].pos[0]][queen["figurw1"].pos[1]] = queen["figurw1"]
piece_board[king["figurw"].pos[0]][king["figurw"].pos[1]] = king["figurw"]
piece_board[bishop["figurw2"].pos[0]][bishop["figurw2"].pos[1]] = bishop["figurw2"]
piece_board[knight["figurw2"].pos[0]][knight["figurw2"].pos[1]] = knight["figurw2"]
piece_board[rook["figurw2"].pos[0]][rook["figurw2"].pos[1]] = rook["figurw2"]




whitecount = 0
blackcount = 0
piececlick = False
enemyclick = False
old_piece = None
old_farbe = "d"
piecerow_old = 99
piececolumn_old = 99

um_countw = 0
um_countb = 0


# Umwandlung von einem Bauern in andere Figuren (wollte noch andere Implementieren aber hat nicht ordentlich Funktioniert)

def umwandlung(y,x):
    global um_countb
    global um_countw
    if piece_board[y][x].art == "bauer" and piece_board[y][x].farbe == "w" and piece_board[y][x].pos[0] == 0:
        um_countw += 1
        
        piece_board[y][x] = queen["figurw%s" %(um_countw+1)]
        chess_board[y][x] = queen["namew"]
        piece_board[y][x].pos = [y,x]
        piece_board[y][x].pos_moves()
    elif piece_board[y][x].art == "bauer" and piece_board[y][x].farbe == "b" and piece_board[y][x].pos[0] == 7:
        um_countb += 1
        piece_board[y][x] = queen["figurb%s" %(um_countb+1)]
        chess_board[y][x] = queen["nameb"]
        piece_board[y][x].pos = [y,x]
        piece_board[y][x].pos_moves()
        
# Mausclick auf andere Figuren wird überprüft

def labelcheck(event):
    global piecerow_old
    global piececolumn_old
    global old_farbe
    global piececlick
    global piecerow
    global piececolumn
    global old_piece
    global whitecount
    global blackcount
    piecerow = event.widget.master.grid_info()["row"]
    piececolumn = event.widget.master.grid_info()["column"]
    piece_board[piecerow][piececolumn].pos_moves()
    piececlick = True
    oldrow_placeholder = piecerow
    oldcolumn_placeholder = piececolumn
    old_piece = piece_board[piecerow][piececolumn]

    #Gegnerische figuren werden eingenommen, falls diese auf den mögl. positionen stehen
    if old_farbe != piece_board[piecerow][piececolumn].farbe and old_farbe != "d":
        if (piece_board[piecerow_old][piececolumn_old].farbe != "b" and whitecount == blackcount) or (blackcount+1 == whitecount and piece_board[piecerow_old][piececolumn_old].farbe == "b"):
            for i in range(len(piece_board[piecerow_old][piececolumn_old].new_pos)):
                if piecerow == piece_board[piecerow_old][piececolumn_old].new_pos[i][0] and piececolumn == piece_board[piecerow_old][piececolumn_old].new_pos[i][1]:
                    if chess_board[piecerow][piececolumn] == "wkönig":
                        open_popup_win("SCHWARZ GEWINNT")
                    elif chess_board[piecerow][piececolumn] == "bkönig":
                        open_popup_win("WEISS GEWINNT")
                    chess_board[piecerow][piececolumn] = chess_board[piecerow_old][piececolumn_old]
                    piece_board[piecerow][piececolumn] = piece_board[piecerow_old][piececolumn_old]
                    piece_board[piecerow_old][piececolumn_old].pos = [piecerow, piececolumn]
                    chess_board[piecerow_old][piececolumn_old] = 0
                    umwandlung(piecerow, piececolumn)
        
                    
                    
            if piece_board[piecerow][piececolumn].farbe == "w":
                whitecount += 1
            if piece_board[piecerow][piececolumn].farbe == "b":
                blackcount += 1
            if whitecount < blackcount:
                blackcount -= 1
            if whitecount-2 >= blackcount:
                whitecount -= 1
        
       
    
    del_pieces()
    wtext = "Weiße Züge:",whitecount
    btext = "Schwarze Züge:", blackcount
    Label(root, text=wtext).place(x=850, y=300)
    Label(root, text=btext).place(x=850, y=350)
    startaufstellung()
    
    old_farbe = old_piece.farbe
    piecerow_old = oldrow_placeholder
    piececolumn_old = oldcolumn_placeholder



# Mausclick auf andere Felder wird überprüft

def framecheck(event):
    global piececlick
    global whitecount
    global blackcount

    # Row und column werte bekommen
    row = event.widget.grid_info()["row"]
    column = event.widget.grid_info()["column"]



    if piececlick:
        if piece_board[piecerow][piececolumn] != 0:
            if (piece_board[piecerow][piececolumn].farbe != "b" and whitecount == blackcount) or (blackcount+1 == whitecount and piece_board[piecerow][piececolumn].farbe == "b"):
                for i in range(len(piece_board[piecerow][piececolumn].new_pos)):
                    if row == piece_board[piecerow][piececolumn].new_pos[i][0] and column == \
                            piece_board[piecerow][piececolumn].new_pos[i][1]:
                        chess_board[row][column] = chess_board[piecerow][piececolumn]
                        piece_board[row][column] = piece_board[piecerow][piececolumn]
                        piece_board[piecerow][piececolumn].pos = [row, column]
                        chess_board[piecerow][piececolumn] = 0
                        umwandlung(row, column)
                piece_board[row][column].pos_moves()
                
                
                if piece_board[row][column].farbe == "w":
                    whitecount += 1
                if piece_board[row][column].farbe == "b":
                    blackcount += 1
                if whitecount < blackcount:
                    blackcount -= 1
                if whitecount-2 >= blackcount:
                    whitecount -= 1
        
    piececlick = False
    
    del_pieces()
    wtext = "Weiße Züge:",whitecount
    btext = "Schwarze Züge:", blackcount
    Label(root, text=wtext).place(x=850, y=300)
    Label(root, text=btext).place(x=850, y=350)
    startaufstellung()



                            




def desImg(list):
    for i in range(8):
        for j in range(8):
            if chess_board[i][j] != 0 and chess_board[i][j] == list:
                frame_list[j][i].widget.destroy()

    # event.widget.destroy() #https://stackoverflow.com/questions/52059974/how-to-delete-or-destroy-label-in-tkinter



    
# Gewinnerpopup
def open_popup_win(text): #https://www.tutorialspoint.com/how-do-i-create-a-popup-window-in-tkinter
    top = Toplevel(root)
    top.geometry("750x250")
    top.title("Spielende")
    Label(top, text=text, font=("Arial 18")).place(x=150, y=80)

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
            frame.bind("<Button-1>", framecheck)
            frame_list[i][
                j] = frame  # https://stackoverflow.com/questions/71576597/how-to-use-tkinter-config-on-a-grid-of-frames


piece_list = [[None for i in range(8)] for j in range(8)]
image_list = [[None for i in range(8)] for j in range(8)]


def addImg(list, img):  # Fügt bilder als labels in die felder ein
    for i in range(8):
        for j in range(8):
            if frame_list[i][j] == list:
                piece = Label(frame_list[i][j], image=img, background=frame_list[i][j]["background"], width=90,
                              height=96)
                piece.pack(expand=TRUE)
                piece.bind("<Button-1>", labelcheck)
                piece_list[i][j] = piece
                image_list[i][j] = img

# Update der Bilder der Figuren
def startaufstellung():
    for i in range(8):
        for j in range(8):
            if chess_board[i][j] == "bbauer":
                addImg(frame_list[i][j], img["bp"])
            elif chess_board[i][j] == "wbauer":
                addImg(frame_list[i][j], img["wp"])
            elif chess_board[i][j] == "wturm":
                addImg(frame_list[i][j], img["wr"])
            elif chess_board[i][j] == "bturm":
                addImg(frame_list[i][j], img["br"])
            elif chess_board[i][j] == "wspringer":
                addImg(frame_list[i][j], img["wkn"])
            elif chess_board[i][j] == "bspringer":
                addImg(frame_list[i][j], img["bkn"])
            elif chess_board[i][j] == "wläufer":
                addImg(frame_list[i][j], img["wb"])
            elif chess_board[i][j] == "bläufer":
                addImg(frame_list[i][j], img["bb"])
            elif chess_board[i][j] == "wkönig":
                addImg(frame_list[i][j], img["wk"])
            elif chess_board[i][j] == "bkönig":
                addImg(frame_list[i][j], img["bk"])
            elif chess_board[i][j] == "wdame":
                addImg(frame_list[i][j], img["wq"])
            elif chess_board[i][j] == "bdame":
                addImg(frame_list[i][j], img["bq"])

            else:
                pass
    

def del_pieces():
    for i in range(8):
        for j in range(8):
            if frame_list[i][j] != None and piece_list[i][j] != None:
                piece_list[i][j].destroy()


def createWin():  # Fenster erstellen (https://www.pythonguis.com/tutorials/create-gui-tkinter/)
    root.title("Schach")
    tk.Button(root, text="Beenden", command=root.destroy).place(x=900, y=200)
    
    createGrid()
    startaufstellung()

    root.mainloop()

createWin()
