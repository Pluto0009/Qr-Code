import gpu
import qrcodevariable

def prepare_code():
    create_position_square(0,0)
    create_position_square(18,0)
    create_position_square(0,18)
    create_alignment_pattern(16,16)
    create_timing_patterns()
    qrcodevariable.qr_code[8][17] = 1  # Always-dark module

def create_position_square(x_start_pos: int, y_start_pos: int):
    for i in range(7):
        qrcodevariable.qr_code[x_start_pos + i][y_start_pos] = 1
        qrcodevariable.qr_code[x_start_pos + i][y_start_pos + 6] = 1
    for i in range(5):
        qrcodevariable.qr_code[x_start_pos][y_start_pos + 1 + i] = 1
        qrcodevariable.qr_code[x_start_pos + 6][y_start_pos + 1 + i] = 1
    for o in range(3):
        for i in range(3):
            qrcodevariable.qr_code[x_start_pos + 2 + i][y_start_pos + 2 + o] = 1

def create_alignment_pattern(x_start_pos: int, y_start_pos: int):
    for i in range(5):
        qrcodevariable.qr_code[x_start_pos + i][y_start_pos] = 1
        qrcodevariable.qr_code[x_start_pos + i][y_start_pos + 4] = 1
    for i in range(3):
        qrcodevariable.qr_code[x_start_pos][y_start_pos + 1 + i] = 1
        qrcodevariable.qr_code[x_start_pos + 4][y_start_pos + 1 + i] = 1
    qrcodevariable.qr_code[x_start_pos + 2][y_start_pos + 2] = 1

def create_timing_patterns():
    for i in range(8, 17):
        if i % 2 == 0:
            qrcodevariable.qr_code[6][i] = 1
            qrcodevariable.qr_code[i][6] = 1