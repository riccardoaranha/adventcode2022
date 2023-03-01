import os, sys, io, argparse

def main(f: io.TextIOWrapper):
    a = []
    lines = f.readlines()
    for line in lines:
        line = line[0:-1]
        a.append([ int(line[i:i+1]) for i in range(0, len(line), 1)])
    
    rows = len(a)
    cols = len(a[0])
    cont = 0

    for i in range(rows):
        cur_vis = -1
        for j in range(cols):
            a[i][j] = [a[i][j], False]
            if a[i][j][0] > cur_vis:
                a[i][j][1] = True
                cur_vis = a[i][j][0]
    for i in range(rows):
        cur_vis = -1
        for j in range(cols-1, -1, -1):
            if a[i][j][0] > cur_vis:
                a[i][j][1] = True
                cur_vis = a[i][j][0]
    for j in range(cols):
        cur_vis = -1
        for i in range(rows):
            if a[i][j][0] > cur_vis:
                a[i][j][1] = True
                cur_vis = a[i][j][0]
    for j in range(cols):
        cur_vis = -1
        for i in range(rows-1, -1, -1):
            if a[i][j][0] > cur_vis:
                a[i][j][1] = True
                cur_vis = a[i][j][0]

    sc_high = 0
    cont1 = 0
    cont2 = [0]*4
    for i in range(rows):
        for j in range(cols):
            cont2 = [0]*4
            if a[i][j][1] == True:
                cont1 +=1

            if i > 0 and i < rows -1 and j > 0 and j < cols -1:

                for m in range (i-1, -1, -1):
                    cont2[0]+=1
                    if a[m][j][0] >= a[i][j][0]:
                        break
                for m in range (i+1, rows, 1):
                    cont2[2]+=1
                    if a[m][j][0] >= a[i][j][0]:
                        break              
                for n in range (j-1, -1, -1):
                    cont2[1]+=1
                    if a[i][n][0] >= a[i][j][0]:
                        break  
                for n in range (j+1, cols, 1):
                    cont2[3]+=1
                    if a[i][n][0] >= a[i][j][0]:
                        break            
                sc = cont2[0]*cont2[1]*cont2[2]*cont2[3]
                if sc > sc_high:
                    sc_high = sc

    print({'part1': cont1, 'part2' : sc_high})
    return {'part1': cont1, 'part2' : sc_high}


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = 'day08',
                                     description = 'Advent of Code Day 08 Template Start ',
                                     epilog = 'Created by Riccardo Aranha')
    parser.add_argument('inputfile', 
                        nargs='?', 
                        default=os.path.join(sys.path[0], "input.txt"), 
                        metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()
    main(args.inputfile)
    args.inputfile.close()