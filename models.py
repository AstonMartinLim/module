"""
The module contains 2 classes: class Enemy and class Player
The module is needed to control the combat logic, lives, levels, mode and scores.
"""

import random
import exceptions
from settings import PLAYER_LIVES, PERMISSIBLE_VALUE, HARD


class Enemy:
    """
    The constructor takes a level. Enemy's health level = enemy's level.
    Class contains two methods:
    Static - select_attack(): returns a random number between one and three.
    Decrease_lives(): decreases the number of lives.
    When life goes to 0 it`s arise an EnemyDown exception.
    """

    def __init__(self, level=1):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """
        The method is needed to select a random number that will be returned
        to the attack method of the class Player
        :return: returns a random number between one and three
        """
        return random.randrange(1, 4)

    def decrease_lives(self):
        """
        The method is needed to reduce the number of enemy lives by 1.
        The method also checks the number of enemy lives, if they reach 0,
        it is raise EnemyDown
        Call in the attack method of the class Player
        :return: None
        """
        self.level -= 1
        print(f'Enemy lost one life. Left {self.level} lives')
        if self.level == 1:
            print('FINISH HIM! HE HAS ONE LAST LIFE!')
        if self.level == 0:
            raise exceptions.EnemyDown


class Player:
    """
    Class is need to construct
    Properties: name, lives, score, allowed_attacks.
    The constructor takes the name of the player.
    The number of lives is indicated from the settings.
    Methods: static fight(), decrease_lives(), attack(), defense()
    """

    def __init__(self, name, lives=PLAYER_LIVES, mode='normal'):
        self.name = name
        self.lives = lives
        self.score = 0
        self.mode = mode

    @staticmethod
    def fight(attack, defense):
        """
        Static method. Needed to determine the results of the battle depending on the choice
        of parameters fight.
        :param attack:
        :param defense:
        :return: returns the result of the round - 0 if a draw, -1 if the attack is unsuccessful,
        1 if the attack is successful
        """
        if attack == 1 and defense == 3 or attack == 2 and defense == 1 or attack == 3 and defense == 2: return -1
        if attack == 1 and defense == 2 or attack == 2 and defense == 3 or attack == 3 and defense == 1: return 1
        if attack == defense: return 0

    def decrease_lives(self):
        """
        The method is needed to reduce the number of player lives by 1.
        The method also checks the number of player lives, if they reach 0,
        it is raise GameOver
        Call in the attack method of the class Player
        :return: None
        """
        self.lives -= 1
        print(f'You lost one life. Left {self.lives} lives')
        if self.lives == 0:
            raise exceptions.GameOver(self.name, self.score, self.mode)

    def attack(self, enemy_obj):
        """
        Method receives input from the user (1, 2, 3), checks if it is valid,
        selects an enemy attack from the enemy_obj object;
        calls the fight() method. If the battle result is 0 - print "It's a draw!",
        if 1 = "You attacked successfully!" and reduces the enemy's lives by 1 if -1 = "You missed!"
        :param self, enemy_obj:
        :return:
        """
        player_choose = int(input('Attack! Choose a fighter\n (1)Shang Tsung\n (2)Liu Kang\n (3)Sub-Zero\n-> '))
        while player_choose not in PERMISSIBLE_VALUE:
            player_choose = int(input('Attack! Choose a fighter\n (1)Shang Tsung\n (2)Liu Kang\n (3)Sub-Zero\n-> '))
        enemy_choose = enemy_obj.select_attack()
        fight_result = Player.fight(player_choose, enemy_choose)
        if fight_result == -1:
            print('You missed!\n')
        if fight_result == 1:
            enemy_obj.decrease_lives()
            if self.mode == 'normal':
                self.score += 1
            else:
                self.score += HARD
            print('You attacked successfully!\n')
        if fight_result == 0:
            print("It's a draw!\n")

    def defence(self, enemy_obj):
        """Method the simular the attack() method, only the enemy attack is passed
        to the fight method first, and if the enemy attacks successfully,
        the player's decrease_lives method is called.
        :param self, enemy_obj:
        :return:
        """
        enemy_choose = enemy_obj.select_attack()
        player_choose = int(input('Defence! Choose a fighter\n (1)Raiden\n (2)Goro\n (3)Scorpion\n-> '))
        while player_choose not in PERMISSIBLE_VALUE:
            player_choose = int(input('Defence! Choose a fighter\n (1)Raiden\n (2)Goro\n (3)Scorpion\n-> '))
        defence_result = Player.fight(enemy_choose, player_choose)
        if defence_result == -1:
            self.decrease_lives()
            print("You missed!\n")
        if defence_result == 1:
            print("You defence successfully!\n")
        if defence_result == 0:
            print("It's a draw!\n")
