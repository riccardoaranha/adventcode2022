import os, sys, io, argparse
#import pprint

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
SCORES = {ROCK: 1, PAPER: 2, SCISSORS: 3}
OPPONENT = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
WIN = 6
DRAW = 3
LOSS = 0

def roundCalc(opp, me):
    score_opp = SCORES[opp]
    score_me = SCORES[me]
    if opp == me:
        score_opp += DRAW
        score_me += DRAW
        result = 'draw'
    elif ((opp == ROCK and me == SCISSORS) or 
          (opp == SCISSORS and me == PAPER) or
          (opp == PAPER and me == ROCK)):
        score_opp += WIN
        score_me += LOSS
        result = 'loose'
    else:
        score_opp += LOSS
        score_me += WIN
        result = 'win'
    #print ('Opponent: %s - Me: %s - Result: %s. ----- Opp Score: %d, MyScore: %d' % (opp, me, result, score_opp, score_me))
    return {'result': result, 'score_opp': score_opp, 'score_me': score_me}

def getChoose(option):
    if option == ROCK:
        return {'win': PAPER, 'draw': ROCK, 'loose': SCISSORS }
    elif option == PAPER:
        return {'win': SCISSORS, 'draw': PAPER, 'loose': ROCK }
    else:
        return {'win': ROCK, 'draw': SCISSORS, 'loose': PAPER }

def main(f: io.TextIOWrapper):
    score_op = 0
    score_my = 0

    options = []
    
    # Part if I want to have all permutations of X, Y and Z.
    #stuff = [ROCK, PAPER, SCISSORS]
    #for subset in itertools.permutations(stuff, 3):
    #    perm = {'X': subset[0], 'Y': subset[1], 'Z': subset[2]}
    #    options.append({'score_me': 0, 'score_opp': 0, 'win': 0, 'draw': 0, 'loose':0, 'decrypt': decrypt})

    # Only otion is the permutation X = Rock, Y = Paper and Z = Scissors
    decrypt = {'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}
    options.append({'score_me': 0, 'score_opp': 0, 'championship_winner':'', 'win': 0, 'draw': 0, 'loose':0, 'decrypt': decrypt})

    decrypt_step2 = {'X': 'loose', 'Y': 'draw', 'Z': 'win'}
    step2 = {'score_me': 0, 'score_opp': 0, 'championship_winner':'', 'win': 0, 'draw': 0, 'loose':0, 'decrypt': None}

    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1 
        split = line.split()
        opp = OPPONENT[split[0]]
        for option in options:
            me = option['decrypt'][split[1]]
            results = roundCalc(opp, me)
            option['score_me'] += results['score_me']
            option['score_opp'] += results['score_opp']
            option[results['result']] += 1

        # Calculation for step 2:  
        me = getChoose(opp)[decrypt_step2[split[1]]]
        results_step2 = roundCalc(opp, me)
        step2['score_me'] += results_step2['score_me']
        step2['score_opp'] += results_step2['score_opp']
        step2[results_step2['result']] += 1  

    for option in options:

        if option['score_me'] > option['score_opp']:
            option['championship_winner'] = 'Me'
        elif option['score_opp'] > option['score_me']:
            option['championship_winner'] = 'Opponent'
        else:
            option['championship_winner'] = 'Draw'
        #pprint.pprint(option)
    #print("--------------------------")
    #print("Step 2:")
    if step2['score_me'] > step2['score_opp']:
        step2['championship_winner'] = 'Me'
    elif step2['score_opp'] > step2['score_me']:
        step2['championship_winner'] = 'Opponent'
    else:
        step2['championship_winner'] = 'Draw'
    #pprint.pprint(step2)
    #print("--------------------------")

    print({'part1': option['score_me'], 'part2' : step2['score_me']})
    return {'part1': option['score_me'], 'part2' : step2['score_me']}

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = 'day02',
                                     description = 'Advent of Code Day 02 Template Start ',
                                     epilog = 'Created by Riccardo Aranha')
    parser.add_argument('inputfile', 
                        nargs='?', 
                        default=os.path.join(sys.path[0], "input.txt"), 
                        metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()
    main(args.inputfile)
    args.inputfile.close()