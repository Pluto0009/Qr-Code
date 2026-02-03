
rows, cols = 25, 25
qr_code = [[0 for _ in range(cols)] for _ in range(rows)]

def prepare_cook():
    create_position_square(0,0)
    create_position_square(19,0)
    create_position_square(0,-19)

def create_position_square(x_start_pos: int, y_start_pos: int):
    for i in range(7):
        qr_code[y_start_pos][x_start_pos + i] = 1
        qr_code[y_start_pos - 6][x_start_pos + i] = 1
    for i in range(5):
        qr_code[y_start_pos - 1 - i][x_start_pos] = 1
        qr_code[y_start_pos - 1 - i][x_start_pos + 6] = 1
    o = 0
    for i in range(3):
        qr_code[y_start_pos - 2 - o][x_start_pos + 2 + i] = 1
        if i == 3:
            i = 0
            o += 1
        if o >= 4:
            break
        