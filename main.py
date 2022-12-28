from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
d = {}
letters = ["a","b","c","d","e","f","g","h"]
root = tk.Tk()

photo = PhotoImage(file= "pieces/blackpawn.png")
bpawn = photo
photo = PhotoImage(file= "pieces/whitepawn.png")
wpawn = photo.


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
        mA[7].configure(image=wpawn)
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

def createGrid(): 

    global mA, mB, mC, mD, mE, mF, mG, mH
    mA, mB, mC, mD, mE, mF, mG, mH = [], [], [], [], [], [], [], []

    mA.append(str(0))
    mB.append(str(0))
    mC.append(str(0))
    mD.append(str(0))
    mE.append(str(0))
    mF.append(str(0))
    mG.append(str(0))
    mH.append(str(0))
    for i in range(8):
        mA.append(str(i+1))
        mB.append(str(i+1))
        mC.append(str(i+1))
        mD.append(str(i+1))
        mE.append(str(i+1))
        mF.append(str(i+1))
        mG.append(str(i+1))
        mH.append(str(i+1))
    
    for i in range(0,8): # Raster erstellen (https://www.pythontutorial.net/tkinter/tkinter-grid/)
        root.columnconfigure(i,weight=1)
        root.rowconfigure(i,weight=1)
        
        
    for i in range(0,8): # Schachmuster erstellen
        if i % 2 == 0:
            for e in range(8,0,-2):
                mA[e] = tk.Label(root, bg="gray", activebackground="gray", text=9-e, anchor=SW) 
                mB[e] = tk.Label(root, bg="white", activebackground="white")
                mC[e] = tk.Label(root, bg="gray", activebackground="gray") 
                mD[e] = tk.Label(root, bg="white", activebackground="white")
                mE[e] = tk.Label(root, bg="gray", activebackground="gray") 
                mF[e] = tk.Label(root, bg="white", activebackground="white")
                mG[e] = tk.Label(root, bg="gray", activebackground="gray") 
                mH[e] = tk.Label(root, bg="white", activebackground="white")
                
                mA[e].grid(column=0, row=e-1, sticky=tk.NSEW)
                mB[e].grid(column=1, row=e-1, sticky=tk.NSEW)
                mC[e].grid(column=2, row=e-1, sticky=tk.NSEW)
                mD[e].grid(column=3, row=e-1, sticky=tk.NSEW)
                mE[e].grid(column=4, row=e-1, sticky=tk.NSEW)
                mF[e].grid(column=5, row=e-1, sticky=tk.NSEW)
                mG[e].grid(column=6, row=e-1, sticky=tk.NSEW)
                mH[e].grid(column=7, row=e-1, sticky=tk.NSEW)
        else:
            for e in range(7,0,-2):
                mA[e] = tk.Label(root, bg="white", activebackground="white", text=9-e, anchor=SW)
                mB[e] = tk.Label(root, bg="gray", activebackground="gray") 
                mC[e] = tk.Label(root, bg="white", activebackground="white")
                mD[e] = tk.Label(root, bg="gray", activebackground="gray") 
                mE[e] = tk.Label(root, bg="white", activebackground="white")
                mF[e] = tk.Label(root, bg="gray", activebackground="gray") 
                mG[e] = tk.Label(root, bg="white", activebackground="white")
                mH[e] = tk.Label(root, bg="gray", activebackground="gray") 
                
                mA[e].grid(column=0, row=e-1, sticky=tk.NSEW)
                mB[e].grid(column=1, row=e-1, sticky=tk.NSEW)
                mC[e].grid(column=2, row=e-1, sticky=tk.NSEW)
                mD[e].grid(column=3, row=e-1, sticky=tk.NSEW)
                mE[e].grid(column=4, row=e-1, sticky=tk.NSEW)
                mF[e].grid(column=5, row=e-1, sticky=tk.NSEW)
                mG[e].grid(column=6, row=e-1, sticky=tk.NSEW)
                mH[e].grid(column=7, row=e-1, sticky=tk.NSEW)
    
    mA[8].configure(text="1a", anchor=SW)
    mB[8].configure(text="b", anchor=SW)
    mC[8].configure(text="c", anchor=SW)
    mD[8].configure(text="d", anchor=SW)
    mE[8].configure(text="e", anchor=SW)
    mF[8].configure(text="f", anchor=SW)
    mG[8].configure(text="g", anchor=SW)
    mH[8].configure(text="h", anchor=SW)
    


    
    

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
    Bauer("w",1)
    root.mainloop()
    

createWin()
