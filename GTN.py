import time
import random
import os
import defs

#hello there! This is GTN (Guess The Number but you dont really guess it you remember it. BUT HEY! No one cares)!  Anyways in this game you have too...                                You guessed it remember and enter proper number (F for people with Dementia) Enjoy the game! :)

#begining
print("Welcome to guess the number!")
time.sleep(1.5)
print("You have to enter the proper number or you loose!")
time.sleep(1.5)
print("Goodluck!")
print(end="\n")
time.sleep(1.5)
defs.Play()
defs.DisplayScoreboard()
time.sleep(3)
defs.create_histogram("scoreboard.txt")#this kind of works but the inputs i gave in scoreboard.txt are crappy. Non the less it works :)
#THE END :(