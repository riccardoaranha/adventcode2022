from unittest import TestCase

from day01.day01 import main as day01
from day02.day02 import main as day02
from day03.day03 import main as day03
from day04.day04 import main as day04
from day05.day05 import main as day05
from day06.day06 import main as day06
from day07.day07 import main as day07
from day08.day08 import main as day08

def dayXX(day, e1, e2, i1, i2):
    f = open('day%02d/example.txt' % day, 'r')
    TestCase().assertDictEqual( {'part1': e1, 'part2' : e2}, globals()['day%02d' % day](f))
    
    f = open('day%02d/input.txt' % day, 'r')
    TestCase().assertDictEqual( {'part1': i1, 'part2' : i2}, globals()['day%02d' % day](f))

def test_day01():
    dayXX(1, 24000, 45000, 75622, 213159)

def test_day02():
    dayXX(2, 15, 12, 13052, 13693)

def test_day03():
    dayXX(3, 157, 70, 7737, 2697)

def test_day04():
    dayXX(4, 2, 4, 475, 825)

def test_day05():
    dayXX(5, 'CMZ', 'MCD', 'TLNGFGMFN', 'FGLQJCMBD')

def test_day06():
    dayXX(6, 11, 26, 1757, 2950)

def test_day07():
    dayXX(7, 95437, 24933642, 2031851, 2568781)

def test_day08():
    dayXX(8, 21, 8, 1543, 595080)
