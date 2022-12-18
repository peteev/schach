from tkinter import *
# https://www.sivakids.de/pygame/
import pygame
from PIL import Image
import sys

# Klassen
"""
# Bauer
class Bauer():
    def __init__(self):
"""

img = Image.open("1200px-Bristol.zoo.capybara.arp.jpg")

img.show()


















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
    
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
        
    screen.blit(text , (width/2+50,height/2))

    pygame.display.update()




