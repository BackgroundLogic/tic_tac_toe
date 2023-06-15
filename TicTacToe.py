from copy import deepcopy
from func import starting_grid, print_grid, turn, check_grid, change_player, play_again

grid = deepcopy(starting_grid)
player = 1

g_round = 1
game_on = True
while game_on:
    # print the current game grid
    print(f"Round {g_round}")
    print_grid(p_grid=grid)

    # take a turn, turn function returns the next player int
    turn(curr_player=player, curr_grid=grid)

    # check if any win condition is met and end game if so
    if check_grid(c_grid=grid):
        # displays winner and prints end game grid
        print(f"Player {player} wins.")
        print_grid(p_grid=grid)
        # sets game state based on user response
        game_on = play_again()
        # resets game
        if game_on:
            grid = deepcopy(starting_grid)
            g_round = 1
    elif g_round == 9:
        # displays all losers and prints end game grid
        print(f"Tie Game\nYou're both losers.")
        print_grid(p_grid=grid)
        # sets game state based on user response
        game_on = play_again()
        # resets game
        if game_on:
            grid = deepcopy(starting_grid)
            g_round = 1
    else:
        g_round += 1
        player = change_player(player)