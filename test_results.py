import unittest  

from day01.day01 import main as day01
from day02.day02 import main as day02
from day03.day03 import main as day03
from day04.day04 import main as day04
from day05.day05 import main as day05
from day06.day06 import main as day06
from day07.day07 import main as day07
from day08.day08 import main as day08
from day09.day09 import main as day09


class TestResults(unittest.TestCase):
    def dayXX(self, day, e1, e2, i1, i2):
        print("\nTesting day %02d" %day)
        f = open('day%02d/example.txt' % day, 'r')
        unittest.TestCase().assertDictEqual( {'part1': e1, 'part2' : e2}, globals()['day%02d' % day](f))
        f.close()
        f = open('day%02d/input.txt' % day, 'r')
        unittest.TestCase().assertDictEqual( {'part1': i1, 'part2' : i2}, globals()['day%02d' % day](f))
        f.close()

    def test_day01(self):
        self.dayXX(1, 24000, 45000, 75622, 213159)

    def test_day02(self):
        self.dayXX(2, 15, 12, 13052, 13693)

    def test_day03(self):
        self.dayXX(3, 157, 70, 7737, 2697)

    def test_day04(self):
        self.dayXX(4, 2, 4, 475, 825)

    def test_day05(self):
        self.dayXX(5, 'CMZ', 'MCD', 'TLNGFGMFN', 'FGLQJCMBD')

    def test_day06(self):
        self.dayXX(6, 11, 26, 1757, 2950)

    def test_day07(self):
        self.dayXX(7, 95437, 24933642, 2031851, 2568781)

    def test_day08(self):
        self.dayXX(8, 21, 8, 1543, 595080)

    def test_day09(self):
        self.dayXX(9, 13, 1, 6464, 2604)

if __name__ == '__main__':
    unittest.main()