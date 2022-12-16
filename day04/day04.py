import os, sys, io, argparse

def sort(elf1, elf2):
    if elf1[0] < elf2[0]:
        elf_sml = elf1
        elf_big = elf2
    elif elf1[0] > elf2[0]:
            elf_sml = elf2
            elf_big = elf1
    else:
        if elf1[1] > elf2[1]:
            elf_sml = elf1
            elf_big = elf2
        else:
            elf_sml = elf2
            elf_big = elf1
    return [elf_sml, elf_big]

def main(f: io.TextIOWrapper):
    lines = f.readlines()
    contained = 0
    overlapped = 0
    for line in lines:

        # Parsing and casting
        elfs = line[:-1].split(',')
        elfs[0] = elfs[0].split('-')
        elfs[0][0] = int(elfs[0][0])
        elfs[0][1] = int(elfs[0][1])
        elfs[1] = elfs[1].split('-')
        elfs[1][0] = int(elfs[1][0])
        elfs[1][1] = int(elfs[1][1])
        
        # Ensure that we can sort, for compare later
        elfs = sort(elfs[0], elfs[1])
        
        # Check if it's full contained
        if elfs[1][1] <= elfs[0][1]:
            contained += 1
        # Check if it has some overlap 
        if elfs[0][1] >= elfs[1][0]:
            overlapped +=1
    
    print("Total contained: %d" % contained)
    print("Total overlapped: %d" % overlapped)


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