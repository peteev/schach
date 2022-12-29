from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
d = {}
letters = ["a","b","c","d","e","f","g","h"]
root = tk.Tk()

photo = PhotoImage(file= "pieces/blackpawn.png")
bpawn_img = photo.subsample(2,2)
photo = PhotoImage(file= "pieces/whitepawn.png")
wpawn_img = photo.subsample(2,2)
photo = PhotoImage(file="pieces/blackrook.png")
bturm_img = photo.subsample(2,2)
photo = PhotoImage(file="pieces/whiterook.png")
wturm_img = photo.subsample(2,2)
photo = PhotoImage(file="pieces/blackknight.png")
bknight_img = photo.subsample(2,2)
photo = PhotoImage(file="pieces/whiteknight.png")
wknight_img = photo.subsample(2,2)
photo = PhotoImage(file="pieces/blackbishop.png")
bbishop_img = photo.subsample(2,2)
photo = PhotoImage(file="pieces/whitebishop.png")
wbishop_img = photo.subsample(2,2)
photo = PhotoImage(file="pieces/blackqueen.png")
bqueen_img = photo.subsample(2,2)
photo = PhotoImage(file="pieces/whitequeen.png")
wqeen_img = photo.subsample(2,2)
photo = PhotoImage(file="pieces/blackking.png")
bking_img = photo.subsample(2,2)
photo = PhotoImage(file="pieces/whiteking.png")
wking_img = photo.subsample(2,2)


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

def createGrid(): 

    # A_Grid = (nur Wert für Button)
    # mA.append(A_Grid[1])
    # mA.append()
    # Versuchen das mit dictionary zu machen (wert hinzufügen wie bei liste aber anders definieren)


    global A_grid, B_grid, C_grid, D_grid, E_grid, F_grid, G_grid, H_grid
    A_grid, B_grid, C_grid, D_grid, E_grid, F_grid, G_grid, H_grid = [], [], [], [], [], [], [], []

    A_grid.append("")
    B_grid.append("")
    C_grid.append("")
    D_grid.append("")
    E_grid.append("")
    F_grid.append("")
    G_grid.append("")
    H_grid.append("")
    for i in range(8):
        A_grid.append("" )
        B_grid.append("")
        C_grid.append("")
        D_grid.append("")
        E_grid.append("")
        F_grid.append("")
        G_grid.append("")
        H_grid.append("")
    
    
        
    
    for i in range(0,8): # Raster erstellen (https://www.pythontutorial.net/tkinter/tkinter-grid/)
        root.columnconfigure(i,weight=1)
        root.rowconfigure(i,weight=1)
        
        
    for i in range(0,8): # Schachmuster erstellen
        if i % 2 == 0:
            for e in range(8,0,-2):
                A_grid[e] = tk.Button(root, bg="gray", activebackground="gray", text=9-e, anchor=SW) 
                B_grid[e] = tk.Button(root, bg="white", activebackground="white")
                C_grid[e] = tk.Button(root, bg="gray", activebackground="gray") 
                D_grid[e] = tk.Button(root, bg="white", activebackground="white")
                E_grid[e] = tk.Button(root, bg="gray", activebackground="gray") 
                F_grid[e] = tk.Button(root, bg="white", activebackground="white")
                G_grid[e] = tk.Button(root, bg="gray", activebackground="gray") 
                H_grid[e] = tk.Button(root, bg="white", activebackground="white")
                
                A_grid[e].grid(column=0, row=e-1, sticky=tk.NSEW)
                B_grid[e].grid(column=1, row=e-1, sticky=tk.NSEW)
                C_grid[e].grid(column=2, row=e-1, sticky=tk.NSEW)
                D_grid[e].grid(column=3, row=e-1, sticky=tk.NSEW)
                E_grid[e].grid(column=4, row=e-1, sticky=tk.NSEW)
                F_grid[e].grid(column=5, row=e-1, sticky=tk.NSEW)
                G_grid[e].grid(column=6, row=e-1, sticky=tk.NSEW)
                H_grid[e].grid(column=7, row=e-1, sticky=tk.NSEW)
        else:
            for e in range(7,0,-2):
                A_grid[e] = tk.Button(root, bg="white", activebackground="white", text=9-e, anchor=SW)
                B_grid[e] = tk.Button(root, bg="gray", activebackground="gray") 
                C_grid[e] = tk.Button(root, bg="white", activebackground="white")
                D_grid[e] = tk.Button(root, bg="gray", activebackground="gray") 
                E_grid[e] = tk.Button(root, bg="white", activebackground="white")
                F_grid[e] = tk.Button(root, bg="gray", activebackground="gray") 
                G_grid[e] = tk.Button(root, bg="white", activebackground="white")
                H_grid[e] = tk.Button(root, bg="gray", activebackground="gray") 
                
                A_grid[e].grid(column=0, row=e-1, sticky=tk.NSEW)
                B_grid[e].grid(column=1, row=e-1, sticky=tk.NSEW)
                C_grid[e].grid(column=2, row=e-1, sticky=tk.NSEW)
                D_grid[e].grid(column=3, row=e-1, sticky=tk.NSEW)
                E_grid[e].grid(column=4, row=e-1, sticky=tk.NSEW)
                F_grid[e].grid(column=5, row=e-1, sticky=tk.NSEW)
                G_grid[e].grid(column=6, row=e-1, sticky=tk.NSEW)
                H_grid[e].grid(column=7, row=e-1, sticky=tk.NSEW)
    
    A_grid[8].configure(text="1a", anchor=SW)
    B_grid[8].configure(text="b", anchor=SW)
    C_grid[8].configure(text="c", anchor=SW)
    D_grid[8].configure(text="d", anchor=SW)
    E_grid[8].configure(text="e", anchor=SW)
    F_grid[8].configure(text="f", anchor=SW)
    G_grid[8].configure(text="g", anchor=SW)
    H_grid[8].configure(text="h", anchor=SW)
    
    global mA, mB, mC, mD, mE, mF, mG, mH
    mA, mB, mC, mD, mE, mF, mG, mH = [], [], [], [], [], [], [], []

    mA.append("")
    mB.append("")
    mC.append("")
    mD.append("")
    mE.append("")
    mF.append("")
    mG.append("")
    mH.append("")
    for i in range(1,9):
        mA.append([A_grid[i]])
        mB.append([B_grid[i]])
        mC.append([C_grid[i]])
        mD.append([D_grid[i]])
        mE.append([E_grid[i]])
        mF.append([F_grid[i]])
        mG.append([G_grid[i]])
        mH.append([H_grid[i]])
    
    for i in range(1,9):
        mA[i].append([1,i])
        mB[i].append([2,i])
        mC[i].append([3,i])
        mD[i].append([4,i])
        mE[i].append([5,i])
        mF[i].append([6,i])
        mG[i].append([7,i])
        mH[i].append([8,i])
        

def startfiguren():
    A_grid[7].configure(image=wpawn_img, anchor=CENTER)
    B_grid[7].configure(image=wpawn_img, anchor=CENTER)
    C_grid[7].configure(image=wpawn_img, anchor=CENTER)
    D_grid[7].configure(image=wpawn_img, anchor=CENTER)
    E_grid[7].configure(image=wpawn_img, anchor=CENTER)
    F_grid[7].configure(image=wpawn_img, anchor=CENTER)
    G_grid[7].configure(image=wpawn_img, anchor=CENTER)
    H_grid[7].configure(image=wpawn_img, anchor=CENTER)
    
    A_grid[8].configure(image=wturm_img, anchor=CENTER)
    B_grid[8].configure(image=wknight_img, anchor=CENTER)
    C_grid[8].configure(image=wbishop_img, anchor=CENTER)
    D_grid[8].configure(image=wqeen_img, anchor=CENTER)
    E_grid[8].configure(image=wking_img, anchor=CENTER)
    F_grid[8].configure(image=wbishop_img, anchor=CENTER)
    G_grid[8].configure(image=wknight_img, anchor=CENTER)
    H_grid[8].configure(image=wturm_img, anchor=CENTER)
    
    A_grid[2].configure(image=bpawn_img, anchor=CENTER)
    B_grid[2].configure(image=bpawn_img, anchor=CENTER)
    C_grid[2].configure(image=bpawn_img, anchor=CENTER)
    D_grid[2].configure(image=bpawn_img, anchor=CENTER)
    E_grid[2].configure(image=bpawn_img, anchor=CENTER)
    F_grid[2].configure(image=bpawn_img, anchor=CENTER)
    G_grid[2].configure(image=bpawn_img, anchor=CENTER)
    H_grid[2].configure(image=bpawn_img, anchor=CENTER)
    
    A_grid[1].configure(image=bturm_img, anchor=CENTER)
    B_grid[1].configure(image=bknight_img, anchor=CENTER)
    C_grid[1].configure(image=bbishop_img, anchor=CENTER)
    D_grid[1].configure(image=bqueen_img, anchor=CENTER)
    E_grid[1].configure(image=bking_img, anchor=CENTER)
    F_grid[1].configure(image=bbishop_img, anchor=CENTER)
    G_grid[1].configure(image=bknight_img, anchor=CENTER)
    H_grid[1].configure(image=bturm_img, anchor=CENTER)
    

    
    

def createWin(): # Fenster erstellen (https://www.pythonguis.com/tutorials/create-gui-tkinter/)
    root.title("Schach")
    root.configure(background="white")
    root.minsize(500,500)
    root.maxsize(1000,750)
    root.geometry("600x600+50+50")
    createGrid()
    
    startfiguren()
    """bruh = Label(image=bpawn)
        bruh.grid(row=1,column=1)"""
    """gray1.configure(image=bpawn)
    
        gray1.bind("<Button-1>", lambda e: buttoncheck())"""
    print(mH[7][1])
    root.mainloop()
    

createWin()
