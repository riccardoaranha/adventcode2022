import os, sys, io, argparse

class Point(object):
    COUNT = 0
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def move(self, direction):
        if direction == 'U':
            self.Y += 1 
        elif direction == 'D':
            self.Y += -1
        elif direction == 'L':
            self.X += -1
        elif direction == 'R':
            self.X += 1
        else:
            raise Exception("Invalid input")

    def moveTowards(self, p):
        if abs(self.X - p.X) == 2 or abs(self.Y - p.Y) == 2:
            self.X += int((p.X - self.X) / (1 if (p.X == self.X) else abs(p.X - self.X)))
            self.Y += int((p.Y - self.Y) / (1 if (p.Y == self.Y) else abs(p.Y - self.Y)))
            

def main(f: io.TextIOWrapper):
    knots_count = 10
    lines = f.readlines()
    knots = [Point(0, 0) for i in range(0, knots_count)]  #array of 9 tails
    unique = set()
    unique.add((0, 0))
    unique2 = set()
    unique2.add((0, 0))
    for line in lines:
        line = line[0:-1]
        x = line.split(' ')
        #print(line)
        for i in range(0, int(x[1])):
            knots[0].move(x[0]) #moves the head
            #print('Head', 0, knots[0].X, knots[0].Y)

            for j in range(1, knots_count):
                knots[j].moveTowards(knots[j-1])
                #print('Tail', j, knots[j].X, knots[j].Y)
            unique.add((knots[1].X, knots[1].Y))
            unique2.add((knots[9].X, knots[9].Y))
            

    part1 = len(unique)
    part2 = len(unique2)
    print({'part1': part1, 'part2' : part2})
    return {'part1': part1, 'part2' : part2}


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = 'dayXX',
                                     description = 'Advent of Code Day XX Template Start ',
                                     epilog = 'Created by Riccardo Aranha')
    parser.add_argument('inputfile', 
                        nargs='?', 
                        default=os.path.join(sys.path[0], "input.txt"), 
                        metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()
    main(args.inputfile)
    args.inputfile.close()