from random import randint  # We import randint to generate random numbers

MINES10 = 10
WIDTH10 = 10
HEIGHT9 = 9
"""We define values for game width, height and number of mines"""


def generate_field(w, h):
    """generating blank field, True/False = mine, number = mines around this field"""
    generated = [[[(False), 0] for i in range(w)] for i in range(h)]
    print("Empty field generated")
    # field_print(generated)
    return generated


def set_mines(num, w, h, field):
    """places mines on the field by changing False to True"""
    check = 0
    mines_list = []
    for i in range(num):
        a = randint(0, w - 1)
        b = randint(0, h - 1)
        while field[b][a][0] is True:
            a = randint(0, w - 1)
            b = randint(0, h - 1)
        mines_list.append(f"{b};{a}")
        field[b][a][0] = True
    print(f"Mine Locations: {mines_list}")
    print("Mined field generated")
    # field_print(field)
    for j in range(h):
        check = check + int(field[j].count([True, 0]))
    print("Minecheck: " + str(check) + " Mines")
    return field


def mine_detection(h, w, field):
    """Detects the number of mines around each field."""
    checklist = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(h):
        for j in range(w):
            x = 0
            for di, dj in checklist:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w:
                    if field[ni][nj][0] is True:
                        x += 1
            field[i][j][1] = x
    print("Detected field generated")
    # field_print(field)
    return field


def field_print(inp):
    """prints readable fields"""
    for i in range(HEIGHT9):
        print(inp[i])


gfield = generate_field(WIDTH10, HEIGHT9)
minefield = set_mines(MINES10, WIDTH10, HEIGHT9, gfield)
playfield = mine_detection(HEIGHT9, WIDTH10, minefield)
vis_field = generate_visible_field(WIDTH10, HEIGHT9)
