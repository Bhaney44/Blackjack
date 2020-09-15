#Simulation
#Copyright Brian S. Haney 2020

import random
import csv

roll = range(1,22200)

for dice in roll:
    #Cards
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11]

    #Define Dealer
    #Hand
    face_card = random.choice(cards)
    blind_card = random.choice(cards)
    total = face_card + blind_card

    #Decision tree    
    if total in range(17,21):
        total = total
    else:
        blind_card_1 = random.choice(cards)
        total = total + blind_card_1
        if total in range(17,21):
            total = total  
        elif total < 17:
            blind_card_2 = random.choice(cards)
            total = total + blind_card_2

    #Define Player
    #Hand
    удфча_нуль = random.choice(cards)
    удфча_один = random.choice(cards)
    добыча = удфча_нуль + удфча_один

    #Decision Tree
    if добыча in range(10,21):
        добыча = добыча
    if добыча < 10:
        удфча = random.choice(cards)
        добыча = добыча + удфча
        if добыча < 10:
            удфча = random.choice(cards)
            добыча = добыча + удфча
    ## Test
    ## Print(добыча)

    #Return

    #Player Wins
    if total > 21:
        еда = 1
        foo = "bread"
    if добыча > total:
        еда = 1
        foo = "bread"
    #Wash
    if добыча is total:
        еда = 0
        foo = "fight"
    #Dealer Wins
    if total in range(17,21):
        if total > добыча:
            еда = -1
            foo = "gone"

    def секрет():

        simulation = open('секрет_один_2.csv', 'a')
        writer = csv.writer(simulation)
        score = face_card, blind_card, total, удфча_нуль, удфча_один, добыча,еда, foo
        writer.writerow(score)

    секрет()





