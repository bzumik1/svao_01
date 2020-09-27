import unittest

from game.GameRPS import Player
from game.GameRPS import Options


class TestGameRPS(unittest.TestCase):
    # OPTIONS
    def test_compare_options(self):
        self.assertEqual(Options.rock > Options.scissors, True)
        self.assertEqual(Options.paper > Options.rock, True)
        self.assertEqual(Options.scissors > Options.paper, True)

    # PLAYER
    def test_player_can_not_be_created_with_invalid_probabilities(self):
        self.assertRaises(ValueError, Player, 0.5, 0.5, 0.5)

    def test_player_plays_with_given_probability(self):
        rock_probability = 0.3
        paper_probability = 0.1
        scissors_probability = 0.6
        test_player = Player(rock_probability, paper_probability, scissors_probability)

        probabilities = [0, 0, 0]
        number_of_played_games = 100000
        for _ in range(number_of_played_games):
            played_option = test_player.play()
            if played_option == Options.rock:
                probabilities[0] += 1
            if played_option == Options.paper:
                probabilities[1] += 1
            if played_option == Options.scissors:
                probabilities[2] += 1
        probabilities = [round(probability/(number_of_played_games//100)) for probability in probabilities]

        self.assertEqual(probabilities, [30, 10, 60])


if __name__ == '__main__':
    unittest.main()
