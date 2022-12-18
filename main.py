from tkinter import *
# https://www.sivakids.de/pygame/
import pygame
from PIL import Image
import sys

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





pygame.init()
# https://pythonbasics.org/tkinter/

# Fenster erstellen (https://www.geeksforgeeks.org/how-to-make-a-pygame-window/)
# Farben
white = (250, 250, 250)
black = (0, 0, 0)
color_light = (170,170,170)
color_dark = (100,100,100)

# Schriftarten
font = pygame.font.SysFont("Arial",35)

# Größe des Fensters
screen = pygame.display.set_mode((500, 500))

# test
width = screen.get_width()
height = screen.get_height()
text = font.render("quit",True, white)



# Name des Fensters
pygame.display.set_caption("Schach")

# Fenster mit Hintergrundfarbe füllen
screen.fill((60,25,60))

# Das Display mit flip aktualisieren
pygame.display.flip()

# Variable für das laufen des Programms
running = True

# spielschleife
while running:
    for event in pygame.event.get():
        # Schließen des Fensters
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
                
    # Position der Maus
    mouse = pygame.mouse.get_pos()
    
    # Erstellung des Quit-Knopfes
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
        
    screen.blit(text , (width/2+50,height/2))

    pygame.display.update()



