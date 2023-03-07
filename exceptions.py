"""
Module for custom exceptions,
has two classes GameOver and EnemyDown
"""


class GameOver(Exception):
    """
    The class is designed to handle cases where the number of lives of player objects
    is reduced to 0. Class has method which save the name player, result and mode regime
    """
    def __init__(self, name, score, mode):
        self.name = name
        self.score = score
        self.mode = mode
        self.save_result()

    def save_result(self):
        """
        The method is needed to save the results of the game in the high score table
        :return: game over message
        """
        with open('scores.txt', 'a') as score_file:
            score_file.write(f"{self.name} || Score: {self.score} point || Mode: {self.mode}\n")
        print(f'You earn {self.score} point')
        return 'Game Over'


class EnemyDown(Exception):
    """
    The class is designed to handle cases where the number of lives of enemy objects
    is reduced to 0.
    """
