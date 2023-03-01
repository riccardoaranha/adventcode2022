import os, sys, io, argparse

curcycle = 0
nextread = 20
strenght = 0
buffer = ''

def cycle(register):
    global curcycle, nextread, strenght, buffer
    curcycle += 1

    x = (curcycle % 40) 
    if x == 0:
        x = 40

    if (register - 1) <= x - 1 and x - 1 <= (register + 1):
        buffer += '#'
    else :
        buffer += '.'
    
    if curcycle == nextread:
        strenght += nextread * register
        #print (curcycle, register, nextread, nextread * register, strenght)
        nextread += 40
    

    if x == 40:
        buffer += '\n'
        
        

def main(f: io.TextIOWrapper):
    global curcycle, nextread, strenght, buffer
    curcycle = 0
    nextread = 20
    strenght = 0
    buffer = ''

    register = 1  

    lines = f.readlines()
    for line in lines:
        line = line[0:-1]
        split = line.split(' ')
        #print(line)
        if split[0] == 'noop':
            cycle(register)
        elif split[0] == 'addx':
            
            x = int(split[1])
            cycle(register)
            cycle(register)
            register += x

    print ({'part1': strenght, 'part2' : ''})
    print(buffer)
    return {'part1': strenght, 'part2' : buffer}


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = 'day10',
                                     description = 'Advent of Code Day 10 Template Start ',
                                     epilog = 'Created by Riccardo Aranha')
    parser.add_argument('inputfile', 
                        nargs='?', 
                        default=os.path.join(sys.path[0], "input.txt"), 
                        metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()
    main(args.inputfile)
    args.inputfile.close()