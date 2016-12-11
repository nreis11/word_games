import os
import sys
import idioms
import unscrambler
import password
import gre_game

# Menu selector for games

def clear_screen(numlines=100):
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)

def start():
    clear_screen()
    print("\nWhich game would you like to play? (Type 'q' to quit)")

    game_list = ['Idioms', 'Unscrambler', 'Password', 'GRE Game']

    for i, game in enumerate(game_list, start=1):
        print(i, game)

    select = 1000
    while select not in range(len(game_list) + 1):
        select = input('\n> ')
        if select == 'q':
            exit(0)
        try:
            select = int(select)
            break
        except Exception:
            print('Please type a valid number.')
    clear_screen()
    if select == 1:
        idioms.start()
    elif select == 2:
        unscrambler.start()
    elif select == 3:
        password.start()
    elif select == 4:
        gre_game.game.start()
    start()

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise SystemExit('Python 3 required!')
    start()
