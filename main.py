from tkinter import *
# https://www.sivakids.de/pygame/
import pygame

pygame.init()
# https://pythonbasics.org/tkinter/

# Fenster erstellen (https://www.geeksforgeeks.org/how-to-make-a-pygame-window/)
# Farben
white = (250, 250, 250)
black = (0, 0, 0)

# Größe des Fensters
screen = pygame.display.set_mode((500, 500))

# Name des Fensters
pygame.display.set_caption("Schach")

# Fenster mit Hintergrundfarbe füllen
screen.fill(white)

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

"""
# Klassen (https://www.w3schools.com/python/python_classes.asp)
# Bauer
class Bauer():
    def __init__(self):
"""
#bruh 