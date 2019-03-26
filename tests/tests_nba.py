from nba.player import Player
import unittest

class NBAAppTests(unittest.TestCase):

    def test_player_name(self):
        player = Player('Lebron','James', 2003, 1, 1)
        self.assertEqual(player.full_name(), 'Lebron James')
        self.assertEqual(player.search_name(), 'lebron james')

if __name__ == "__main__":
    unittest.main()
