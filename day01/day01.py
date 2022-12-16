import os, sys, io, argparse
from collections import namedtuple
from sortedcontainers import SortedList

Pair = namedtuple("Pair", ["value", "id"])

def printTopX(list : SortedList, x):
    total = 0
    print("--------------------------")
    print ("Top %d Cals" % x)
    i = 0
    for qty in list.islice(stop=x):
        i += 1
        total += qty.value
        print("[%dº][id=%d]: %d" % (i, qty.id, qty.value))
    print("Total Top %d: %d" % (x, total))
    print("--------------------------")
    
def main(f: io.TextIOWrapper):
    lines = f.readlines()
  
    curElf = 0
    totalCals = 0
    qties = SortedList(key=lambda x: -x.value)
    id = 0

    for line in lines:
        if line == "\n":
            qties.add(Pair(curElf, id))
            id += 1
            curElf = 0
        else:
            current = int(line)
            curElf += current
            totalCals += current

    printTopX(qties, 1)
    printTopX(qties, 3)
    print("Elfs count: %d" % qties.__len__())
    print("Total Cals: %d" % totalCals)


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = 'day01',
                                     description = 'Advent of Code Day 01 Template Start ',
                                     epilog = 'Created by Riccardo Aranha')
    parser.add_argument('inputfile', 
                        nargs='?', 
                        default=os.path.join(sys.path[0], "input.txt"), 
                        metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()
    main(args.inputfile)
    args.inputfile.close()