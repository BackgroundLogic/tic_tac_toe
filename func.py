from pc_player import move_selector

starting_grid = [
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3'],
    ['C1', 'C2', 'C3'],
]
row = {
    "A": 0,
    "B": 1,
    "C": 2,
}
col = {
    "1": 0,
    "2": 1,
    "3": 2,
}
p1 = ' X'
p2 = ' O'



def print_grid(p_grid):
    """
    Prints to console the data in provided grid with bars and dashes between to create a TicTacToe board
    Grid should be provided as a 3x3 list of lists
    :param p_grid:
    :return:
    """
    last_row = p_grid[-1]
    for x in p_grid:
        print(f"{x[0]} | {x[1]} | {x[2]}")
        if x != last_row:
            print(f"- - - - - - -")


def check_grid(c_grid):
    """
    Returns True if TicTacToe win condition is met in the provided 3x3 grid,
    grid should be a list of lists
    :param c_grid:
    :return:
    """
    # check rows
    for g_row in c_grid:
        if g_row[0] == g_row[1] == g_row[2]:
            return True
    # check columns
    for g_col in range(3):
        if c_grid[0][g_col] == c_grid[1][g_col] == c_grid[2][g_col]:
            return True
    if c_grid[0][0] == c_grid[1][1] == c_grid[2][2]:
        return True
    if c_grid[0][2] == c_grid[1][1] == c_grid[2][0]:
        return True
    return False


def check_string(player_input, g_grid):
    """
    Takes player input and a grid in the form of a list of lists
    returns True if input is in the Grid
    :param player_input:
    :param g_grid:
    :return:
    """
    if any(player_input in x for x in g_grid):
        return True
    else:
        print("Invalid move, space may be taken already \nplease try again.")
        return False


def change_player(curr_player):
    """
    Takes a player variable as an int and changes it to the next player
    :param curr_player:
    :return:
    """
    if curr_player == 1:
        return 2
    else:
        return 1


def turn(curr_player, curr_grid, ai_on):
    """
    Takes a player variable as an int and a 3x3 grid in the format of a list of lists
    :param ai_on:
    :param curr_player:
    :param curr_grid:
    :return:
    """
    if ai_on and curr_player == 2:
        input_list = move_selector(curr_grid)
    else:
        print(f"\nPlayer {curr_player}'s turn.\n")
        # loop until player submits a valid move
        valid_move = False
        input_string = str
        while not valid_move:
            # take input from the player
            input_string = input('Enter a Row Letter and Column Number: ').upper().replace(" ", "")
            # check if player input is a valid move
            valid_move = check_string(player_input=input_string, g_grid=curr_grid)
        input_list = list(input_string)

    # Check who the current player is and place mark on board accordingly
    if curr_player == 1:
        curr_grid[row[input_list[0]]][col[input_list[1]]] = p1
    else:
        curr_grid[row[input_list[0]]][col[input_list[1]]] = p2


def play_again():
    """
    Checks if the players would like to go again
    returns True if they do
    returns False if they don't
    :return:
    """
    invalid_response = True
    while invalid_response:
        player_response = input("Would you like to play again? (Y/N) \n").upper()
        if player_response == 'Y':
            return True
        elif player_response == 'N':
            print("returning false")
            return False
        else:
            print("Invalid response, please type (Y/N)")


def pc_player():
    invalid_response = True
    while invalid_response:
        pc_answer = input("Are you playing against another human,\n"
                      "or would you like to play against a PC player?\n"
                      "PC Player on? (Y/N): ").upper()
        if pc_answer == "Y":
            return True
        elif pc_answer == "N":
            return False
        else:
            print("Invalid response, please type (Y/N)")