import os, sys, io, argparse


def find(line, buffer_size):
    buffer = line[0:buffer_size]
    for index, char in enumerate(line[buffer_size:]):
        buffer = buffer[1:buffer_size] + char
        found = False
        for i in range(len(buffer) - 1):
            if buffer[i] in buffer[i+1:buffer_size]:
                found = True
                break
        if found == False:
            return index + buffer_size + 1
    return -1

def main(f: io.TextIOWrapper):
    lines = f.readlines()
    for line in lines:
        line = line[0:-1]
        buffer1, buffer2 = 4, 14
        index1 = find(line, buffer1)
        index2 = find(line, buffer2)
        #print ("First char with buffer %d is %c, on index %d" % (buffer1, line[index1], index1))
        #print ("First char with buffer %d is %c, on index %d" % (buffer2, line[index2], index2))
    
    print ({'part1': index1, 'part2' : index2})
    return {'part1': index1, 'part2' : index2}
        
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