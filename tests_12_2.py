import unittest

# Предполагаем, что классы Runner и Tournament уже определены.

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __eq__(self, other):
        return self.name == other.name

    def run(self, distance):
        return distance / self.speed

    def walk(self, distance):
        return distance / (self.speed / 2)  # Например, скорость при ходьбе в два раза меньше


class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        for runner in self.runners:
            time = runner.run(self.distance)
            results[time] = runner.name
        # Сортируем результаты по времени
        sorted_results = dict(sorted(results.items()))
        return sorted_results


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(cls.all_results[key])

    def test_tournament_usain_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        self.all_results[1] = tournament.start()
        self.assertTrue(list(self.all_results[1].values())[-1] == "Ник")

    def test_tournament_andrey_nik(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        self.all_results[2] = tournament.start()
        self.assertTrue(list(self.all_results[2].values())[-1] == "Ник")

    def test_tournament_usain_andrey_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        self.all_results[3] = tournament.start()
        self.assertTrue(list(self.all_results[3].values())[-1] == "Ник")


if __name__ == '__main__':
    unittest.main()