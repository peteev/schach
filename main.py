from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

photo = PhotoImage(file= "pieces/blackpawn.png")
bpawn = photo.subsample(1,1)
photo = PhotoImage(file= "pieces/whitepawn.png")
wpawn = photo.subsample(1,1)
photo = PhotoImage(file="pieces/transparent.png")
trans = photo.subsample(1,1)


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
        self.bauer_startpos()
        self.pos = [self.posX, self.posY]
        
        # Umwandlung zu anderen Figuren sobald Bauer die andere Spielseite erreicht (funktioniert nicht)
        self.umwandlung = False
        
        
        match self.farbe, self.posY:
            case "w",8:
                self.umwandlung = True
            case "b",1:
                self.umwandlung = True
            case _:
                self.umwandlung = False

    def bauer_startpos(self):
        self.bauer_startposX()
        self.bauer_startposY()
    def bauer_startposX(self):
        # Startpositionen der verschiedenen Bauern 
        self.posX = self.num
        return self.posX
    def bauer_startposY(self):
        if self.farbe == "w":
            self.posY = 2
        else:
            self.posY = 7
        return self.posY
        
class Springer(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
    
    def springer_startpos(self, farbe, num):
        if num == 1:
            self.posX = 2
        else:
            self.posX = 7
        if farbe == "w":
            self.posY = 1
        else:
            self.posY = 8
        
class Laeufer(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
        
    def laeufer_startpos(self, farbe, num):
        if num == 1:
            self.posX = 3
        else:
            self.posX = 6
        if farbe == "w":
            self.posY = 1
        else:
            self.posY = 8
        
class Turm(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
        
    def turm_startpos(self, farbe, num):
        if num == 1:
            self.posX = 1
        else:
            self.posX = 8
        if farbe == "w":
            self.posY = 1
        else:
            self.posY = 8
        
class Dame(Figur):
    def __init__(self, farbe):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
        
    def dame_startpos(self, farbe):
        self.posX = 4
        if farbe == "w":
            self.posY = 1
        else:
            self.posY = 8
            
class Koenig(Figur):
    def __init__(self, farbe):
        super().__init__(farbe)
        self.pos = [self.posX, self.posY]
        
    def koenig_startpos(self, farbe):
        self.posX = 5
        if farbe == "w":
            self.posY = 1
        else:
            self.posY = 8










def buttoncheck():
    print("bruh")
    gray1.configure(image="")

def createGrid(): 
    
    for i in range(0,8): # Raster erstellen (https://www.pythontutorial.net/tkinter/tkinter-grid/)
        root.columnconfigure(i,weight=1)
        root.rowconfigure(i,weight=1)
        
        
    for i in range(0,8): # Schachmuster erstellen
        if i % 2 == 0: # gerade
            for e in range(0,8,2):
                globals()["black{0}".format(i)] = tk.Label(root, bg="gray", activebackground="gray", text=str(["black{0}".format(i)]), anchor=SE) # https://www.w3schools.com/python/python_dictionaries.asp
                globals()["black{0}".format(i)].grid(column=i, row=e+1, sticky=tk.NSEW)
                globals()["white{0}".format(i)] = tk.Label(root, bg="white", activebackground="white")
                globals()["white{0}".format(i)].grid(column=i, row=e, sticky=tk.NSEW)
        else:
            for e in range(0,8,2):
                globals()["black{0}".format(i)] = tk.Label(root, bg="gray", activebackground="gray") 
                globals()["black{0}".format(i)].grid(column=i, row=e, sticky=tk.NSEW)
                globals()["white{0}".format(i)] = tk.Label(root, bg="white", activebackground="white")
                globals()["white{0}".format(i)].grid(column=i, row=e+1, sticky=tk.NSEW)


        
        

def createWin(): # Fenster erstellen (https://www.pythonguis.com/tutorials/create-gui-tkinter/)
    root.title("Schach")
    root.configure(background="white")
    root.minsize(500,500)
    root.maxsize(1000,750)
    root.geometry("600x600+50+50")
    createGrid()
    """bruh = Label(image=bpawn)
        bruh.grid(row=1,column=1)"""
    """gray1.configure(image=bpawn)

        gray1.bind("<Button-1>", lambda e: buttoncheck())"""
    black0.configure(image=bpawn)
    root.mainloop()
    

createWin()
