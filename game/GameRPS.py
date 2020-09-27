from enum import Enum, unique
import random

from console.Console import Color


class Player:
    """Player class represents probabilities with which player plays."""
    def __init__(self, rock_probability, paper_probability, scissors_probability):
        if rock_probability + paper_probability + scissors_probability != 1:
            raise ValueError("the sum of probabilities must be 1")
        self.rock = rock_probability
        self.paper = paper_probability
        self.scissors = scissors_probability

    def play(self):
        """Returns randomly played option based on probabilities."""
        random_number = random.random()
        if random_number <= self.rock:
            return Options.rock
        if self.rock < random_number <= (self.rock+self.paper):
            return Options.paper
        if (self.rock+self.paper) < random_number:
            return Options.scissors


@unique
class Options(Enum):
    """Represents options which player can play in game rock, paper, scissors."""
    rock = 1
    paper = 2
    scissors = 3

    def __gt__(self, other):
        if self == Options.rock:
            if other == Options.scissors:
                return True
        if self == Options.paper:
            if other == Options.rock:
                return True
        if self == Options.scissors:
            if other == Options.paper:
                return True
        else:
            return False


def play_rsp(player1, player2, number_of_games):
    """Serves for simulating N games with given players in game rock, paper, scissors."""
    statistics = [0, 0, 0]
    for i in range(number_of_games):
        print(Color.UNDERLINE + f"Starting {i+1}. game:" + Color.END)
        player1_option = player1.play()
        print(f"\tPlayer1 has played {player1_option.name}.")
        player2_option = player2.play()
        print(f"\tPlayer2 has played {player2_option.name}.")

        if player1_option == player2_option:
            print(Color.BOLD + "\t\tIt's a draw!" + Color.END)
            statistics[0] += 1
        elif player1_option > player2_option:
            print(Color.BOLD + "\t\tPlayer1 has won!" + Color.END)
            statistics[1] += 1
        else:
            print(Color.BOLD + "\t\tPlayer2 has won!" + Color.END)
            statistics[2] += 1
    print(f"\n{Color.BOLD}Statistics: {Color.END}From {number_of_games} games player1 won {statistics[1]} games, "
          f"player2 won {statistics[2]} and {statistics[0]} games ended in a draw.")
    return statistics
