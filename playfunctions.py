#
# :date: 2018-10-18
# :author: Andre Stephens
# :copyright: GPL v2 or later
#
#

import random
import itertools
import sys
import time

player = 'PLAYER 1'
scorecard = {'PLAYER 1': {'turn': True, 'score': 0},
             'PLAYER 2': {'turn': False,'score': 0}}
msg_input_play1 = "Would you like to buy a vowel? Enter 1 to spin, 2 to buy vowel... "
msg_input_play2 = "INVALID PLAY. Please choose either 1 for constonant, 2 for vowel or q to quit... "

def make_spin(wheel):
    rnum = random.choice(range(40,50,1))
    count = rnum
    secs = 0.1
    spinner = []
    for i in range(rnum):
        spinner.append(random.choice(wheel))
    for i in itertools.cycle(spinner):
        if count >= 30:
            secs = 0.05
        if 15 <= count < 30:
            secs = 0.075
        if 6 <= count < 15:
            secs = 0.15
        if 3 <= count < 6:
            secs = 0.3
        if 1 <= count < 3:
            secs = 0.6
        if count < 1:
            secs = 1.2
        if count == 0:
            break
        sys.stdout.write('\r' + str(i) + ' '*10)
        sys.stdout.flush()
        time.sleep(secs)
        count -=1
    time.sleep(0.2)
    print("\rSpin: {}".format(i))
    return i

def clean_output():
    if os.name == 'nt':
    # for windows
        _ = os.system('cls')
    # for mac and linux
    else: 
        _ = system('clear') 

def switch_players(player):
    if player == 'PLAYER 1':
        return 'PLAYER 2'
    return 'PLAYER 1'

def print_score(final=False):
    msg_score = "Player {}'s current winning is ${}." 
    if final:
        msg_score = "FINAL SCORE: YOU WON ${}. PLAYER 2 WON ${}. Good game!"
    time.sleep(1)
    p1_score = scorecard['PLAYER 1']['score']
    p2_score = scorecard['PLAYER 2']['score']
    print(msg_score.format('1',p1_score))
    time.sleep(0.5)
    print(msg_score.format('2',p2_score))

def buy_vowel():
    time.sleep(2)
    letter = game.choose_vowel()
    return letter

def bad_spin(spin):
    if spin == 'bankrupt':
        print(player, "lost all their money. Oh no! :( :( :(")
        if scorecard[player]['score'] > 0:
            scorecard[player]['score'] = 0
    if spin == 'lose turn' or spin == 'bankrupt':
        print(player, "lost turn. Sorry... :(")
        return True
    return False

def get_play(player):
    play = str(input(msg_input_play1))
    while play not in '12q':
        play = input(msg_input_play2)
    return play


