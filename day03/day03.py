import os, sys, io, argparse


def main(f: io.TextIOWrapper):
    lines = f.readlines()
    total_prio = 0
    total_group = 0
    i = 0
    group = [None]*3
    for line in lines:
        line = line[0:-1]
        mid = int((len(line))/2)
        comp1 = line[:mid]
        comp2 = line[mid:]
        group[i] = line
        #print(i)
        i += 1

        for char in comp1:
            if char in comp2:
                prio = ord(char) - ord('a') + 1 if (char >= 'a' and char <= 'z') else ord(char) - ord('A') + 27
                total_prio += prio
                #print(char, prio)
                break
        if i == 3:
            i = 0
            for char in group[0]:
                if char in group[1]:
                    if char in group[2]:
                        badge = ord(char) - ord('a') + 1 if (char >= 'a' and char <= 'z') else ord(char) - ord('A') + 27
                        total_group += badge
                        #print("Group:", char, badge)
                        break
    #print("Total prio: %d" % total_prio)
    #print("Total group: %d" % total_group)
    print({'part1': total_prio, 'part2' : total_group})
    return {'part1': total_prio, 'part2' : total_group}

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