import os, sys, io, argparse

stacks1 = []
stacks2 = None

def load_line(line):
    line = line[0:-1]
    chunk_size = 4
    x = [ line[i:i+chunk_size] for i in range(0, len(line), chunk_size) ]
    if len(x) != len(stacks1):
        for i in range(len(x)):
            stacks1.append([])
    i = 0
    for k in x:
        k = k.strip(' ').strip('[').strip(']')
        if k != '':
            (stacks1[i]).append(k)
        i += 1

def main(f: io.TextIOWrapper):
    lines = f.readlines()
    for line in lines:
        if '[' in line:
            load_line(line)    
        elif not 'move' in line and stacks2 is None:
            stacks2 = []
            for stack in stacks1:
                stacks2.append(stack.copy())

        elif 'move' in line:
            data = line.split()
            qty = int(data[1])
            src = int(data[3]) - 1 
            dst = int(data[5]) - 1
            for i in range(qty):
                x = stacks1[src].pop(0)
                stacks1[dst].insert(0, x)
            
            for i in range(qty-1, -1, -1):
                x = stacks2[src].pop(i)
                stacks2[dst].insert(0, x)

    finals1 = ''  
    finals2 = ''       
    for stack in stacks1:
        finals1 += stack[0]
    for stack in stacks2:
        finals2 += stack[0]
    
    print("Top of pile, CrateMover 9000:")
    print(finals1)    
    print("Top of pile, CrateMover 9001:")
    print(finals2)

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