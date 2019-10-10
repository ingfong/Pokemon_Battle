import pygame
from tkinter import *
import subprocess
from poke import Poke
import random
import time
from PIL import ImageTk, Image


root = Tk()
canvas = Canvas(root, bg="blue", height=430, width=730)
canvas.pack()

player = Poke('fire')
enemy = Poke('water')
pygame.mixer.init()

pygame.mixer.music.load("Battle_music.wav") 
pygame.mixer.music.play()

def enemy_move():
    
    move = random.randint(1,4)
    
    if move == 1:
        enemy.pound(player)
        subprocess.call(["afplay", "oof.wav"])
        if player.health <= 0:
            subprocess.call(["afplay", "win_battle.wav"])
            print("Player has been defeated!")
            quit()
        else:
            print("Player Health:%s\nEnemy Health:%s\n"%(player.health,enemy.health))
            
    elif move == 2:
        enemy.scratch(player)
        subprocess.call(["afplay", "scratch.wav"])
        if player.health <= 0:
            subprocess.call(["afplay", "win_battle.wav"])
            print("Player has been defeated!")
            quit()
        else:
            print("Player Health:%s\nEnemy Health:%s\n"%(player.health,enemy.health))
            
    elif move == 3:
        enemy.growl(player)
        subprocess.call(["afplay", "growl.wav"])
        if player.health <= 0:
            subprocess.call(["afplay", "win_battle.wav"])
            print("Player has been defeated!")
            quit()
        else:
            print("Player Health:%s\nEnemy Health:%s\n"%(player.health,enemy.health))
            
    elif move == 4:
        enemy.bubble(player)
        subprocess.call(["afplay", "bubble.wav"])
        if player.health <= 0:
            subprocess.call(["afplay", "win_battle.wav"])
            print("Player has been defeated!")
            quit()
        else:
            print("Player Health:%s\nEnemy Health:%s\n"%(player.health,enemy.health))

    
def scratch():
    player.scratch(enemy)
    subprocess.call(["afplay", "slash.wav"])
    if enemy.health <= 0:
        pygame.mixer.music.stop()
        subprocess.call(["afplay", "win_battle.wav"])
        print("Enemy has been defeated!")
        quit()
    else:
        print("Player Health:%s\nEnemy Health:%s\n"%(player.health,enemy.health))
        enemy_move()


def pound():
    player.pound(enemy)
    subprocess.call(["afplay", "oof.wav"])
    if enemy.health <= 0:
        pygame.mixer.music.stop()

        subprocess.call(["afplay", "win_battle.wav"])
        print("Enemy has been defeated!")
        quit()
    else:
        print("Player Health:%s\nEnemy Health:%s\n"%(player.health,enemy.health))
        enemy_move()

def growl():
    player.growl(enemy)
    subprocess.call(["afplay", "growl.wav"])
    if enemy.health <= 0:
        pygame.mixer.music.stop()
        subprocess.call(["afplay", "win_battle.wav"])
        print("Enemy has been defeated!")
        quit()
    else:
        print("Player Health:%s\nEnemy Health:%s\n"%(player.health,enemy.health))
        enemy_move()
        
def ember():
    player.ember(enemy)
    subprocess.call(["afplay", "ember.wav"])
    #subprocess.call(["afplay", "creeper.wav"])
    if enemy.health <= 0:
        pygame.mixer.music.stop()
        subprocess.call(["afplay", "win_battle.wav"])
        print("Enemy has been defeated!")
        quit()
    else:
        print("Player Health:%s\nEnemy Health:%s\n"%(player.health,enemy.health))
        enemy_move()

display_text = Label(root, text= 'Charmander used POUND.')
display_text.pack()
display_text.text = "ahhh"     


background = PhotoImage(file ="pokemon_battle.ppm")
la = Label(root, image=background)
la.place(x=0, y=0)


b = Button(root,text = "Scratch", command = scratch)
b.config(height = 2, width = 10)
b.pack()
b.place(x=100, y=380)


c = Button(root,text = "Pound", command = pound)
c.config(height = 2, width = 10)
c.pack()
c.place(x=100, y=320)

d = Button(root,text = "Ember", command = ember)
d.config(height = 2, width = 10)
d.pack()
d.place(x=230, y=320)

e = Button(root,text = "Growl", command = growl)
e.config(height = 2, width = 10)
e.pack()
e.place(x=230, y=380)



root.mainloop()
pygame.quit()