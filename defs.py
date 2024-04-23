import time
import os
import random
import re
"""
Code made by: Komandor98 aka Grzegorz Matczak
fav gaem: Among us

Copyright: NONE (but pls dont copy)
Trademark: idk BUT ITS IMPORTANT for selling cheese. Because if you got it from teacher you have permition to trade with one item of your choice (or teachers) and make 1% of profit YAY I LOVE CAPITALISM

"""
def Win(name,score):#wins duh
    with open("scoreboard.txt", "r",encoding="utf-8") as file:#opens file
        lines = file.readlines()

    scores = {}
    for line in lines:
        parts = line.strip().split()
        if len(parts) % 2 == 0:
            for i in range(0, len(parts), 2):
                scores[parts[i]] = int(parts[i+1])

    if name not in scores:
        AddScore(name, score)
    elif scores[name] < score:
        scores[name] = score
        with open("scoreboard.txt", "w",encoding="utf-8") as file:
            for name, score in scores.items():
                file.write(f"{name} {score}\n")

def AddScore(name,score):

    file = open("scoreboard.txt", "a",encoding="utf-8")
    file.write(" " + name + " " + str(score))

def Paragraph(): 
    with open("paragraph.txt", "rb") as file:
        content = file.read().decode("utf-8").split("\n")


    words = []

    for element in content:
        words.append(element.split(" "))

    i = 0
    x = 0
    y = 0
    letter = ""
    while i < len(words):
        while x < len(words[i]):
            while y < len(words[i][x]):
                letter = words[i][x][y]
                print(letter, end="", flush=True)
                time.sleep(0.2 + (random.uniform(-0.05, 0.02)))
                y+=1
            time.sleep(len(words[i][x]) / random.randint(70 ,150))
            print(end=" ")
            y=0
            x+=1
        x = 0
        print(end="\n")
        time.sleep(1.5 + random.uniform(-0.1 , 0.3))
        i+=1


def Play():

    wrong = 0
    hasWon=0

    digit = 1
    score = 0
    #score=9 #test
    


    while wrong == 0 or hasWon == 1: #starting loop
        

        a = 0
        genNumstr= ""
        while a <= digit-1:#generates random number

            genNum= random.randint(1,9)

            genNumstr+= str(genNum)
            a+=1

        print(genNumstr)
        time.sleep(2+(0.5*digit))
        os.system("clear")
        os.system("cls")
        
        enterednum= input("Enter number: ")

        if int(enterednum) == int(genNumstr):#adds 1 more digit to generated number
            digit+=1
            score+=1
            print("Correct!")

        else:
            wrong=1 #loose
            print("You Lost!")
            print("Your score is " + str(score))
            print("The number was: " + str(genNumstr) + " You entered: " +str(enterednum))
            

        if score == 10: #win you can change it if you want too the old one was 7
            hasWon = 1
            
        
        if hasWon == 1 or wrong ==1:#asking to save progres
            choice = input("Save your progres? Y/N: ")
            if choice == "Y" or choice == "y":

                name = input("What's your name?: ")#I added name to the end because it more resambles old games and it saves time while testing the code

                name = name.replace(" ", "_")

                Win(name,score)
                if hasWon == 1:
                    Paragraph()
                break
            if choice == "N" or choice == "n":
                if hasWon == 1:
                    Paragraph()
                break
    return score

"""def DisplayScoreboard(): #old code dont use! ESPECIALLY YOU SLEEPY STEVE!
    with open("scoreboard.txt","r") as file:
        scoreboard = file.read()
    dict = {}
    scoreboard = scoreboard.split()
    if len(scoreboard) % 2 != 0:
        print("Invalid scoreboard format.")
        return
    for i in range(0, len(scoreboard), 2):
        print(scoreboard[i],": ",scoreboard[i+1])"""

def DisplayScoreboard():
    print("------------------------")
    print("Scoreboard")
    print("------------------------")

    with open("scoreboard.txt", "r",encoding="utf-8") as file:
        lines = file.readlines()

    scores = {}
    for line in lines:
        parts = line.strip().split()
        if len(parts) % 2 == 0:
            for i in range(0, len(parts), 2):
                scores[parts[i]] = int(parts[i+1])

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    count = 0
    for name, score in sorted_scores:
        if count == 10:
            break
        print(name, ": ", score)
        count += 1

def create_histogram(file_name):
    print("------------------------")
    print("Stats thingy")
    print("------------------------")
    # Read the file contents
    with open(file_name) as f:
        file_contents = f.read()

    # Split the file contents into a list of names and scores
    parts = file_contents.split()

    # Initialize a dictionary to count the occurrences of each score
    score_counts = {i: 0 for i in range(1, 11)}

    # Loop through the scores and increment the count for each score
    for i in range(1, len(parts), 2):
        score = int(parts[i])
        if score >= 1 and score <= 10:
            score_counts[score] += 1

    # Print the histogram
    for i in range(1, 11):
        print(f"{i}: {'#' * score_counts[i]}")
