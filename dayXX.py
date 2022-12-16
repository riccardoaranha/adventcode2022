import os, sys, io, argparse


def main(f: io.TextIOWrapper):
    print(f.read())
    


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