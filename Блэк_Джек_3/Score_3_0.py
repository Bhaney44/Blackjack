import csv

csvfile = open('секрет_один_3.csv', 'r')


read = csv.reader(csvfile)

dealer_score = 0
player_score = 0
games = 0

for row in read:
    keyword_0 = str('bread')
    keyword_1 = str('fight')
    keyword_2 = str('gone')
    if keyword_0 in row:
        player_score += 1
        games += 1
    if keyword_1 in row:
        games += 1
    if keyword_2 in row:
        dealer_score += 1
        games += 1
        
print('dealer wins:', dealer_score)
print('player wins:', player_score)
print('games:', games)

