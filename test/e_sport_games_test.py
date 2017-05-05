import unittest
import datetime
from database.dao import DAO
from model.game import Game


class ESportGamesTest(unittest.TestCase):


    def test_01_insert(self):
        entry = Game(name="League of Legends", description="League of Legends is a MOBA game. The most played game of the world.", created_at=datetime.datetime.now())

        DAO.create(entry)

        game = DAO.find(Game, name="League of Legends")[0]

        self.assertIsNotNone(game)

    def test_02_find(self):

       games = DAO.find_all(Game)

       self.assertGreater(len(games), 0)

    def test_03_update(self):

        game = DAO.find(Game, name="League of Legends")[0]

        date_time = datetime.datetime.now()

        game.updated_at = date_time

        DAO.update(game)

        game_updated = DAO.find(Game, name="League of Legends")[0]

        self.assertEqual(game.updated_at, game_updated.updated_at)

    def test_04_remove(self):

        games = DAO.find_all()

        for game in games:
            DAO.delete(game)

        games = DAO.find_all()

        self.assertEqual(len(games), 0)


if __name__ == '__main__':
    unittest.main()