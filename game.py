"""
The module is necessary to receive initial information from the user,
on the basis of which the game process will be launched
"""

from exceptions import EnemyDown, GameOver
from models import Enemy, Player
from settings import HELP, MODE, HARD


def menu():
    """
    Function for displaying the program menu
    function takes: information from the user
    :return: menu item or command to start the game
    """

    print("""Game menu:
    START - for beginning the game (type 'start')
    HELP - shows a list of possible commands (type 'help')
    MODE - show information about mode regime (type 'mode')
    SHOW SCORES - show table of scores (type 'show_scores')
    EXIT - exit the game (type 'exit')""")
    menu_input = input('-> ')
    if menu_input == 'start':
        print('The fight has begun. Mortal Kombat!')
        return 'start'
    if menu_input == 'help':
        print(HELP, '\n')
    if menu_input == 'mode':
        print(MODE, '\n')
    if menu_input == 'show_scores':
        with open('scores.txt', 'r') as score_file:
            read_scores = score_file.read()
            print(read_scores)
    if menu_input == 'exit':
        raise KeyboardInterrupt
    else:
        menu()


def select_mode():
    """
    Function to select the difficulty of the game
    :return: player choice normal mode or hard mode
    """
    print('''Select game mode:
    NORMAL (type 'normal')
    HARD (type 'hard')''')
    mode = input('-> ')
    if mode == 'normal':
        return 'normal_mode'
    elif mode == 'hard':
        return 'hard_mode'
    else:
        print('Coward! are you scared? Make a choice')
        select_mode()


def play():
    """
    function to start the game process
    creates objects of class player and class enemy
    In an infinite loop, methods of attacking and defending the player object are used
    In case of victory, arise EnemyDown exception, the game level is increased by 1,
    created a new object of the Enemy class with a new level
    :return: None
    """
    player_name = False
    while not player_name:
        player_name = input('Type your name: ')
        if player_name.isalpha() and len(player_name) > 3:
            player_name = player_name
        else:
            player_name = False
            print('Name must be more than 3 character and consist of only alphabetic character')
    menu()
    selected_mode = select_mode()
    player = None
    level = 0
    enemy = None
    if selected_mode == 'normal_mode':
        player = Player(player_name)
        level = 1
        enemy = Enemy(level)
    if selected_mode == 'hard_mode':
        player = Player(player_name, mode='hard')
        level = 4
        enemy = Enemy(level)
    while True:
        try:
            Player.attack(player, enemy)
            Player.defence(player, enemy)
        except EnemyDown:
            level += 1
            print(f'You kill enemy! Go to the next level. Now enemy level is {level}')
            enemy = Enemy(level)
            if player.mode == 'normal':
                player.score += 5
            else:
                player.score += (5*HARD)


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!')
