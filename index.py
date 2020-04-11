from Questions import Questions as q
import time
from TimeThread import TimeThread as tt
import random
import os

#Print the instructions how to play the game
def show_instructions():
    print("Hello, welcome to the game \"Who is more smart?\"")
    print("""
The instructions are:
1) I´m going to give you a question.
2) The que2stion has 4 posible answers, you've got to select the answer that you think is the correct one
Oh! I forgot to tell you something, each player has 10 seconds to response each question. You've got to be fast!
3) I'm going to tell you the correct answer and after that I´m going to show you the score of each player""")

#get the numbers of players
#Create and initialize the vector which is saving the score of each player    
def get_nplayers():
    num =int(input("\nCould you tell me the numbers of players: "))

    players = list()
    for i in range(num):
        players.append(0)

    return num,players
#create a vector and select 10 numbers in a range of 1 and 10
#These numbers are the numbers of question the players are going to answer
def get_randoms():
    random_nums = list()
    while len(random_nums)<10:
        r = random.randint(1,10)
        if not r in random_nums:
            random_nums.append(r)
    return random_nums

#Print the score at the moment
def get_score():
    global score
    print("\n----------Score---------")
    for s in range(len(score)):
        print("Player {}: {} ptos".format(s,score[s]))
    print("--------------------------\n")


# def create_and_show_time():
#     win = Tk()
#     win.mainloop()

show_instructions()
nPlayers,score = get_nplayers()
questions = get_randoms() 

os.system("cls")

for i in questions:
    print("Pregunta "+str(i))
    for j in q[i].keys():
        if j!="correct":
           print(q[i][j])
    print("\n")
    for k in range(nPlayers):
        t = tt()
        t.setDaemon(True)
        t.start()
        print("\nplayer "+str(k+1))
        ans = input()
        t.stop()
        w = Tk()
        w.mainloop()
        time.sleep(3)
        w.destroy()
        get_score()

      
       
        
        

        
    