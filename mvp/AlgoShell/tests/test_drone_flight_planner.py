import unittest
from solutions import calc_drone_min_energy

class DroneFlightPlanner(unittest.TestCase):
    def test_case_1(self):
        route = [[0,1,19]]

        expected = 0
        actual = calc_drone_min_energy(route)

        self.assertEqual(expected, actual)

    def test_case_2(self):
        route = [[0,2,10],[10,10,8]]

        expected = 0
        actual = calc_drone_min_energy(route)

        self.assertEqual(expected, actual)

    def test_case_3(self):
        route = [[0,2,6],[10,10,20]]

        expected = 14
        actual = calc_drone_min_energy(route)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        route = [[0,2,10],[3,5,0],[9,20,6],[10,12,15],[10,10,8]]

        expected = 5
        actual = calc_drone_min_energy(route)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        route = [[0,2,2],[3,5,38],[9,20,6],[10,12,15],[10,10,8]]

        expected = 36
        actual = calc_drone_min_energy(route)

        self.assertEqual(expected, actual)

    def test_case_6(self):
        route = [[0,2,10],[3,5,9],[9,20,6],[10,12,2],[10,10,10],[10,10,2]]

        expected = 0
        actual = calc_drone_min_energy(route)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()