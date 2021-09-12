import random

grid = [' '] * 9


# This holds all the filled and empty spaces currently representing the board
# Initially set to represent an empty board


def apply_move(character, position):
    grid[position] = character


# This function returns whether or not the position being checked is empty
def check_for_empty(position):
    return grid[position] == ' '


def check_if_full(grid):
    return grid.count(' ') == 0


# Produce a visual of the current state of the board
def print_grid(grid):
    print('     |     |')
    print('  ' + grid[0] + '  |  ' + grid[1] + '  |  ' + grid[2])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + grid[3] + '  |  ' + grid[4] + '  |  ' + grid[5])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + grid[6] + '  |  ' + grid[7] + '  |  ' + grid[8])
    print('     |     |\n')


# Checks if the player has won by checking if there's 3 of their character in a
# row, column, or diagonal
def check_for_win(grid, char):
    return ((grid[0] == char and grid[1] == char and grid[2] == char) or
            # Top row
            (grid[3] == char and grid[4] == char and grid[5] == char) or
            # Bottom row
            (grid[6] == char and grid[7] == char and grid[8] == char) or
            # Middle row
            (grid[0] == char and grid[3] == char and grid[6] == char) or
            # Left column
            (grid[1] == char and grid[4] == char and grid[7] == char) or
            # Middle column
            (grid[2] == char and grid[5] == char and grid[8] == char) or
            # Right column
            (grid[0] == char and grid[4] == char and grid[8] == char) or
            # Diagonal top left corner to bottom right corner
            (grid[6] == char and grid[4] == char and grid[2] == char))
    # Diagonal bottom left corner to top right corner


def user_move():
    running = True

    # Loop until a valid move is completed
    while running:
        placement = input('Select a position to put an X (0-8): ')
        try:
            placement = int(placement)
            # Make sure number is between 0-8
            if 0 <= placement < 9:

                # Check if the space chosen isn't occupied
                if check_for_empty(placement):
                    apply_move('X', placement)
                    running = False
                else:
                    print('Space is occupied, please pick another space!')
            else:
                print('Must be a number from 0-8, please pick another number!')
        except:
            print("Must be a number, please pick a number from 0-8!")


def computer_move():
    potential_moves = [i for i, char in enumerate(grid) if char == ' ']
    # Creates a list of possible moves by checking for empty spaces

    # Computer first checks to make winning move or prevent user's winning move
    for option in ['O', 'X']:
        for k in potential_moves:
            grid_copy = grid.copy()
            grid_copy[k] = option
            if check_for_win(grid_copy, option):
                return k

    # Computer looks to take any open corners randomly
    open_corners = []
    for k in potential_moves:
        if k in [0, 2, 6, 8]:
            open_corners.append(k)
    if len(open_corners):
        return random.choice(open_corners)

    # Computer looks to take the center if it's open
    if 4 in potential_moves:
        return 4

    # Computer looks to take any remaining open spots
    open_spaces = []
    for k in potential_moves:
        if k in [1, 3, 5, 7]:
            open_spaces.append(k)
    if len(open_spaces):
        return random.choice(open_corners)

    return -1


# This function controls the main operations of the game
def main():
    print_grid(grid)
    while not (check_if_full(grid)):
        if not (check_for_win(grid, 'O')):
            user_move()
            print_grid(grid)
        else:
            print('The computer wins this time!')
            return

        if not (check_for_win(grid, 'X')):
            move = computer_move()
            if move == -1:
                print('Tie Game!')
            else:
                apply_move('O', move)
                print('Computer placed an O in position', move, '\n')
                print_grid(grid)
        else:
            print('You win! Good Job!')
            return


main()
