# The aim of this file is to use the computer oponent's check_possible_moves() method to pre-calculate the best first and second moves
# The first move is calculated as the best option for an empty grid.
# The second move is calculated as the best response to three possible scenarios: the opposing player picks either the centre square, a corner square or a middle-of-a-side square.
from noughts_and_crosses import Game, ComputerOpponent

# Case 1: the first move
game1 = Game()
comp1 = ComputerOpponent(game1, 'X')
ranked_moves1 = comp1.check_possible_moves()
print(' --- Ranked options for first move ---')
for move in ranked_moves1:
    print(f'{move[0]}: {move[1]}')
print(' ------ \n')

# Cases 2-4: The second move after the user has chosen (2) the centre square, (3) a corner square, and (4) a middle-of-a-side square

CASES = (('the centre', 4),
         ('a corner', 0),
         ('a middle-of-a-side', 1)
        )

for case in CASES:
    game_n = Game()
    game_n.moveList.append(case[1])
    comp_n = ComputerOpponent(game_n, 'O')
    ranked_moves_n = comp_n.check_possible_moves()
    # Moves are ranked in order of the best result for 'X', so need to be reversed for 'O'
    ranked_moves_n.reverse()
    print(f' --- Ranked options for second move (after player 1 takes {case[0]} square)  ---')
    for move in ranked_moves_n:
        print(f'{move[0]}: {move[1]}')
    print(' ------ \n')
