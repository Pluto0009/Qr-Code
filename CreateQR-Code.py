
import gpu

rows, cols = 25, 25
qr_code = [[0 for _ in range(cols)] for _ in range(rows)]

def prepare_code():
    create_position_square(0,0)
    create_position_square(18,0)
    create_position_square(0,18)

def create_position_square(x_start_pos: int, y_start_pos: int):
    for i in range(7):
        qr_code[x_start_pos + i][y_start_pos] = 1
        qr_code[x_start_pos + i][y_start_pos + 6] = 1
    for i in range(5):
        qr_code[x_start_pos][y_start_pos + 1 + i] = 1
        qr_code[x_start_pos + 6][y_start_pos + 1 + i] = 1
    for o in range(3):
        for i in range(3):
            qr_code[x_start_pos + 2 + i][y_start_pos + 2 + o] = 1

prepare_code()
gpu.erstelle_pixel_bild(qr_code)
        