#
# :date: 2018-10-18
# :author: Andre Stephens
# :copyright: GPL v2 or later
#
#
#
# Example usage:
# ~ python play.py words.txt
#


import argparse
from playfunctions import *
from gamebuild import WordsOfFortune, BuildWF

msg_end_game = '\n\n\n*******GAME ENDED. GOODBYE!********'
solved = False

def play(game, player='PLAYER 1'):
    
    game.choose_word()
    game.make_current_word()
    wheel = build.get_wheel()

    while not solved:
        #clean_output()
        game.print_header(player)        

        if player == 'PLAYER 2':
            letter = game.computer_choose_letter()
            if letter.upper() in 'AEIOU':
                print('PLAYER 2 would like to buy a vowel.')
            else:
                spin = make_spin(wheel)
                if bad_spin(spin):
                    player = switch_players(player)
                    continue
            time.sleep(2)
            print('PLAYER 2 chose', letter.upper())
        else:
            play = get_play(player)
            if play == 'q' or play == 'Q':
                print(msg_end_game)
                break
            elif play == '2':
                letter = game.buy_vowel()
            else:
                spin = make_spin(wheel)
                if bad_spin(spin):
                    player = switch_players(player)
                    continue
                letter = game.choose_consonant()

        game.update_available_letters()
        if letter in game.get_word():
            n_guess = game.update_current_word()
            if n_guess == 1:
                msg_found = ">>>>>>> YES! {} {}."
            else:
                msg_found = ">>>>>>> YES! {} {}'s."
            print(msg_found.format(n_guess, letter.upper()))
            time.sleep(2)
            print(game.get_current_word())
            old_score = scorecard[player]['score']
            time.sleep(2)
            scorecard[player]['score'] = game.update_score(spin, old_score, n_guess)
        else:
            time.sleep(2)
            print(">>>>>>> SORRY. NO {}.".format(letter.upper()))
            old_score = scorecard[player]['score']
            player = switch_players(player)

        # check solution
        if game.is_solved():
            print(player, 'solved puzzle for: {} and earned a $2000 bonus'.format(game.get_word()))
            scorecard[player]['score'] =+ 2000
            time.sleep(2)
            print_score(final=True)
            break

        print_score()


def play_round(BuildWF, fname):
    BuildWF.load_words(fname)
    BuildWF.build_wheel()
    BuildWF.make_available_letters()
    return BuildWF



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename', 
        type=str,
        help='text file with words to be loaded')
    args = parser.parse_args()

    build = BuildWF()
    game = play_round(build, args.filename)
    play(game)
