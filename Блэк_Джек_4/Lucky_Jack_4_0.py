#LuckyJack
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
label7 = Label(master, text = 'Player Total', relief = 'groove', width = 20)

#Blanks
blank1 = Entry(master, relief = 'groove', width = 20)
blank2 = Entry(master, relief = 'groove', width = 20)
blank3 = Entry(master, relief = 'groove', width = 20)
blank4 = Entry(master, relief = 'groove', width = 20)
blank5 = Entry(master, relief = 'groove', width = 20)
blank6 = Entry(master, relief = 'groove', width = 20)

#Player
label8 = Label(master, text = 'Player', relief = 'groove', width = 20)
label9 = Label(master, text = 'Card 0', relief = 'groove', width = 20)
label10 = Label(master, text = 'Card 1', relief = 'groove', width = 20)
label11 = Label(master, text = 'Hit', relief = 'groove', width = 20)
label12 = Label(master, text = 'Player Total', relief = 'groove', width = 20)
#Blanks
blank7 = Entry(master, relief = 'groove', width = 20)
blank8 = Entry(master, relief = 'groove', width = 20)
blank9 = Entry(master, relief = 'groove', width = 20)
blank10 = Entry(master, relief = 'groove', width = 20)

#Score
label9 = Label(master, text = 'Player Total', relief = 'groove', width = 20)
label10 = Label(master, text = 'Dealer Total', relief = 'groove', width = 20)
label11 = Label(master, text = 'Chips', relief = 'groove', width = 20)
label12 = Label(master, text = 'Cost', relief = 'groove', width = 20)
label13 = Label(master, text = 'Return', relief = 'groove', width = 20)
label14 = Label(master, text = 'Lucky Jack', relief = 'groove', width = 20)

#Blanks
blank11 = Entry(master, relief = 'groove', width = 20)
blank12 = Entry(master, relief = 'groove', width = 20)
blank13 = Entry(master, relief = 'groove', width = 20)
blank14 = Entry(master, relief = 'groove', width = 20)
blank15 = Entry(master, relief = 'groove', width = 20)

#def deal():

#def hit():

#Buttons
button0 = Button(master, text = 'Hit', relief = 'groove', width = 20, command = hit)
button1 = Button(master, text = 'Deal', relief = 'groove', width = 20, command = deal)

#Geometry
#


#Static Properties
master.title('LuckyJack')
