#LuckyJack Table
#Copyright Brian S. Haney 2020

#Import Random
#Import Prototype GUI and Data Storage Library
from tkinter import *
from tkinter.messagebox import *
import csv

#Factor Labels
master = Tk()

#Dealer
#Labels
label0 = Label(master, text = 'Dealer', relief = 'groove', width = 20)
label1 = Label(master, text = 'Open Card', relief = 'groove', width = 20)
label3 = Label(master, text = 'Secret Card', relief = 'groove', width = 20)
label4 = Label(master, text = 'Hit', relief = 'groove', width = 20)
label5 = Label(master, text = 'Hit', relief = 'groove', width = 20)
label6 = Label(master, text = 'Hit', relief = 'groove', width = 20)
label7 = Label(master, text = 'Dealer Score', relief = 'groove', width = 20)
#Blanks
blank1 = Entry(master, relief = 'groove', width = 20)
blank2 = Entry(master, relief = 'groove', width = 20)
blank3 = Entry(master, relief = 'groove', width = 20)
blank4 = Entry(master, relief = 'groove', width = 20)
blank5 = Entry(master, relief = 'groove', width = 20)
blank6 = Entry(master, relief = 'groove', width = 20)
#blank7 = Entry(master, relief = 'groove', width = 20)

#Player
#Labels
label8 = Label(master, text = 'Player', relief = 'groove', width = 20)
label9 = Label(master, text = 'Card 0', relief = 'groove', width = 20)
label10 = Label(master, text = 'Card 1', relief = 'groove', width = 20)
label11 = Label(master, text = 'Hit', relief = 'groove', width = 20)
label12 = Label(master, text = 'Player Score', relief = 'groove', width = 20)
#Blanks
blank8 = Entry(master, relief = 'groove', width = 20)
blank9 = Entry(master, relief = 'groove', width = 20)
blank10 = Entry(master, relief = 'groove', width = 20)
blank11 = Entry(master, relief = 'groove', width = 20)

#Scoreboard
#Labels
label13 = Label(master, text = 'Chips', relief = 'groove', width = 20)
#label14 = Label(master, text = 'Cost', relief = 'groove', width = 20)
label15 = Label(master, text = 'Bet', relief = 'groove', width = 20)
label16 = Label(master, text = 'Lucky Jack Table', relief = 'groove', width = 20)
label17 = Label(master, text = 'Prize', relief = 'groove', width = 20)
#label18 = Label(master, text = 'Dealer Score', relief = 'groove', width = 20)
#label19 = Label(master, text = 'Player Score', relief = 'groove', width = 20)

#Blanks
blank12 = Entry(master, relief = 'groove', width = 20)
blank13 = Entry(master, relief = 'groove', width = 20)
blank14 = Entry(master, relief = 'groove', width = 20)
blank15 = Entry(master, relief = 'groove', width = 20)
blank16 = Entry(master, relief = 'groove', width = 20)
blank17 = Entry(master, relief = 'groove', width = 20)

#Functions
def deal():
    
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
         2,3,4,5,6,7,8,9,10,10,10,10,11]

    #Dealer Hand
    #Face
    face_card = random.choice(cards)
    #Insert to
    blank1.grid( row = 13, column = 2, padx = 10 )
    #Secret
    blind_card = random.choice(cards)
    total = face_card + blind_card
    
    #Player Hand
    удфча_нуль = random.choice(cards)
    blank8.grid( row = 13, column = 4, padx = 10 )
    #Insert to blank
    
    удфча_один = random.choice(cards)
    blank9.grid( row = 14, column = 4, padx = 10 )
    #Insert to blank
    
    добыча = удфча_нуль + удфча_один
    blank11.grid( row = 18, column = 4, padx = 10 )
    #Insert to blank
    
    print(deal)

def hit():

    #Dealor Decision tree
    secret_card_0 = random.choice(cards)
    blind_card_1 = random.choice(cards)
    blind_card_2 = random.choice(cards)
    blind_card_3 = random.choice(cards)
    total = face_card + secret_card_0
    if total in range(17,21):
        total = total
    else:
        blind_card_1 = random.choice(cards)
        total = total + blind_card_1
        if total in range(17,21):
            total = total  
        if total < 17:
            total = total + blind_card_2
            if total < 17:
                total = total + blind_card_3
            
    #Update and Insert Total
    print(hit)
    
    #Player
    добыча = удфча_нуль + удфча_один
    #Get data from dealer
    удфча = random.choice(cards)
    #Little luck -> insert to "hit" blank
    добыча = добыча + удфча
    #Update and insert to total blank

    #Prize
    #Insert prize system
    #Player Wins
    if total > 21:
        еда = int(10)
    if добыча > total:
        еда = int(10)
    #Wash
    if добыча is total:
        еда = int(0)
    #Dealer Wins
    if total in range(17,21):
        if total > добыча:
            еда = int(0)

    prize = еда
    #Insert to blank

    #Update chips
    chip_total = get_chips()
    new_total = get_chips + prize
    #Insert to blank
    

def buy_chips():
    chip_total = get_chips()
    new_total = get_chips + 10
    #Insert to chips

    #Test
    ##print('10 chips')

#Buttons
button0 = Button(master, text = 'Hit', relief = 'groove', width = 20, command = hit)
button1 = Button(master, text = 'Deal', relief = 'groove', width = 20, command = deal)
button2 = Button(master, text = 'More Chips', relief = 'groove', width = 20, command = buy_chips)

#Geometry
#Dealer
label0.grid( row = 11, column = 1, padx = 10 )
label1.grid( row = 13, column = 1, padx = 10 )
label3.grid( row = 14, column = 1, padx = 10 )
label4.grid( row = 15, column = 1, padx = 10 )
label5.grid( row = 16, column = 1, padx = 10 )
label6.grid( row = 17, column = 1, padx = 10 )
label7.grid( row = 18, column = 1, padx = 10 )

blank1.grid( row = 13, column = 2, padx = 10 )
blank2.grid( row = 14, column = 2, padx = 10 )
blank3.grid( row = 15, column = 2, padx = 10 )
blank4.grid( row = 16, column = 2, padx = 10 )
blank5.grid( row = 17, column = 2, padx = 10 )
blank6.grid( row = 18, column = 2, padx = 10 )

#Player
label8.grid( row = 11, column = 3, padx = 10 )
label9.grid( row = 13, column = 3, padx = 10 )
label10.grid( row = 14, column = 3, padx = 10 )
label11.grid( row = 15, column = 3, padx = 10 )
label12.grid( row = 18, column = 3, padx = 10 )

blank8.grid( row = 13, column = 4, padx = 10 )
blank9.grid( row = 14, column = 4, padx = 10 )
blank10.grid( row = 15, column = 4, padx = 10 )
blank11.grid( row = 18, column = 4, padx = 10 )

#Scoreboard
label13.grid( row = 11, column = 6, padx = 10 )
#label14.grid( row = 6, column = 3, padx = 10 )
label15.grid( row = 14, column = 6, padx = 10 )

label16.grid( row = 1, column = 3, padx = 40 )
label17.grid( row = 17, column = 6, padx = 30 )
#label18.grid( row = 6, column = 2, padx = 10 )
#label19.grid( row = 6, column = 2, padx = 10 )

blank12.grid( row = 13, column = 6, padx = 10 )
#blank13.grid( row = 7, column = 3, padx = 10 )
blank14.grid( row = 15, column = 6, padx = 10 )
#blank15.grid( row = 4, column = 1, padx = 10 )
#blank16.grid( row = 4, column = 5, padx = 10 )
blank17.grid( row = 18, column = 6, padx = 10 )

button0.grid( row = 12, column = 3, columnspan = 1)
button1.grid( row = 12, column = 1, columnspan = 1)
button2.grid( row = 12, column = 6, columnspan = 1)

#Static Properties
master.title('LuckyJack')
