import os, sys, io, argparse
from tinytree import Tree

cur_node : Tree = None
tree : Tree = None

def treatCommand(line):
    global tree, cur_node
    x = line.split(' ')
    if x[0] == '$' and x[1] == 'cd':
        if x[2] == '/':
            if tree == None:
                tree = Tree()
                tree.__setattr__('name', '/')
                tree.__setattr__('type', 'dir')
                cur_node = tree
        elif x[2] == '..':
            if not cur_node.parent == None:
                cur_node = cur_node.parent
        else:
            for child in cur_node.children:
                if child.__getattribute__('name') == x[2]:
                    cur_node = child
                    return

def addDir(line):
    global tree, cur_node

    x = line.split(' ')
    if x[0] == 'dir':
        child = Tree()
        child.__setattr__('name', x[1])
        child.__setattr__('type', 'dir')
        cur_node.addChild(child)

def addFile(line):
    global tree, cur_node

    x = line.split(' ')
    if x[0].isnumeric():
        child = Tree()
        child.__setattr__('name', x[1])
        child.__setattr__('type', 'file')
        child.__setattr__('size', int(x[0]))
        cur_node.addChild(child)

def walk_print(node : Tree, spaces):
    print('-'*spaces*2, 
          node.__getattribute__('type'),
          node.__getattribute__('name'),
          node.__getattribute__('size'))

    for child in node.children:
        walk_print(child,spaces + 1)

def walk_calc(node : Tree):
    if node.__getattribute__('type') == 'file': 
        return node.__getattribute__('size')
    else:
        size = 0
        for child in node.children:
            size += walk_calc(child)
        node.__setattr__('size', size)
        return size

def walk_filter01(node:Tree, limit):
    if node.__getattribute__('type') == 'file': 
        return 0
    else:
        size = node.__getattribute__('size')
        if size > limit:
            size = 0
        for child in node.children:
            size += walk_filter01(child, limit)
        return size

def walk_filter02(node:Tree, min_deletion, cur_min):
    if node.__getattribute__('type') == 'file': 
        return cur_min
    else:
        size = node.__getattribute__('size')
        if size < cur_min and size >= min_deletion:
            cur_min = size
        for child in node.children:
            cur_min = walk_filter02(child, min_deletion, cur_min)
        return cur_min



def main(f: io.TextIOWrapper):
    global tree, cur_node
    cur_node = None
    tree = None

    lines = f.readlines()
    
    for line in lines:
        line = line[0:-1]
        if line[0] == '$':
            treatCommand(line)
        elif line[0:3] == 'dir':
            addDir(line)
        elif line[0].isnumeric():
            addFile(line)
    walk_calc(tree)
    #walk_print(tree, 1)
    part1 = walk_filter01(tree, 100000)
    #print('Part 1 - Size: ', part1)

    site_total = tree.__getattribute__('size')
    capacity =  70000000
    necessity = 30000000
    min_deletion = site_total - (capacity - necessity)
    part2 = walk_filter02(tree, min_deletion, capacity)
    #print('Part 2 - Size: ', part2)
    
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