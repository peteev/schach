from tkinter import ttk
import tkinter as tk

from PIL import Image


# Klassen (https://www.w3schools.com/python/python_classes.asp; https://www.w3schools.com/python/python_inheritance.asp)
class Figur:
    def __init__(self, farbe):
        self.farbe = farbe
        self.posX = 0
        self.posY = 0
        
class Bauer(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
        self.bauer_startpos(farbe,num)
        
        # Umwandlung zu anderen Figuren sobald Bauer die andere Spielseite erreicht (funktioniert nicht)
        self.umwandlung = False
        
        
        match self.farbe, self.posY:
            case "w",8:
                self.umwandlung = True
            case "b",1:
                self.umwandlung = True
            case _:
                self.umwandlung = False
        
        

        
    def bauer_startpos(self, farbe, num):
        # Startpositionen der verschiedenen Bauern 
        self.posX = num
        if farbe == "w":
            self.posY = 2
        else:
            self.posY = 7
        
class Springer(Figur):
    def __init__(self, farbe, num):
        super().__init__(farbe)
    
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
        
    def dame_startpos(self, farbe):
        self.posX = 4
        if farbe == "w":
            self.posY = 1
        else:
            self.posY = 8
            
class Koenig(Figur):
    def __init__(self, farbe):
        super().__init__(farbe)

    def koenig_startpos(self, farbe):
        self.posX = 5
        if farbe == "w":
            self.posY = 1
        else:
            self.posY = 8




root = tk.Tk()
def createGrid(): 
    
    for i in range(0,8): # Raster erstellen
        root.columnconfigure(i,weight=1)
        root.rowconfigure(i,weight=1)
        
        
    for i in range(0,8): # Schachmuster erstellen
        d = {}
        if i % 2 != 0:
            for e in range(0,8,2):
                d["black{0}".format(i)] = tk.Button(root, bg="black") # https://www.w3schools.com/python/python_dictionaries.asp
                d["black{0}".format(i)].grid(column=i, row=e+1, sticky=tk.NSEW)
                d["white{0}".format(i)] = tk.Button(root, bg="white")
                d["white{0}".format(i)].grid(column=i, row=e, sticky=tk.NSEW)
        else:
            for e in range(0,8,2):
                d["black{0}".format(i)] = tk.Button(root, bg="black") 
                d["black{0}".format(i)].grid(column=i, row=e, sticky=tk.NSEW)
                d["white{0}".format(i)] = tk.Button(root, bg="white")
                d["white{0}".format(i)].grid(column=i, row=e+1, sticky=tk.NSEW)


def createWin(): # Fenster erstellen (https://www.pythonguis.com/tutorials/create-gui-tkinter/)
    root.title("Schach")
    root.configure(background="white")
    root.minsize(500,500)
    root.maxsize(1000,750)
    root.geometry("600x600+50+50")
    createGrid()
    root.mainloop()


createWin()



