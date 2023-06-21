from random import choice
p1 = ' X'
p2 = ' O'


def move_selector(curr_grid):
    move_list = find_valid_moves(curr_grid=curr_grid)
    return list(choice(move_list))


def find_valid_moves(curr_grid):
    move_list = []
    for g_row in curr_grid:
        for cell in g_row:
            if cell == p1:
                pass
            elif cell == p2:
                pass
            else:
                move_list.append(cell)
    return move_list
