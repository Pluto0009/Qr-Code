import qrcodevariable
import math

masked_qr_codes = []

def apply_masking():
    for i in range(8):
        masked_qr_codes[i] = qrcodevariable.qr_code
        apply_mask(i)
    

def apply_mask(number: int):
    
    for col_index, column in enumerate(qrcodevariable.fill_order_grid):
            for row_index, pos in enumerate(column):
                if pos != 0:
                    match_number = -1
                    match number:
                        case 0:
                            match_number = math.fmod(row_index + col_index, 2)
                        case 1:
                            match_number = math.fmod(row_index, 2)
                        case 2:
                            match_number = math.fmod(col_index, 3)
                        case 3:
                            match_number = math.fmod(row_index + col_index, 3)
                        case 4:
                            match_number = math.fmod(math.floor(row_index / 2) + math.floor(col_index / 3), 2)
                        case 5:
                            match_number = math.fmod(row_index * col_index, 2) + math.fmod(row_index * col_index, 3)
                        case 6:
                            match_number = math.fmod(math.fmod(row_index * col_index, 2) + math.fmod(row_index * col_index, 3), 2)
                        case 7:
                            match_number = math.fmod(math.fmod(row_index + col_index, 2) + math.fmod(row_index * col_index, 3), 2)
                    
                    if match_number == 0:
                        if masked_qr_codes[number][col_index][row_index] == 0:
                            masked_qr_codes[number][col_index][row_index] = 1
                        else:
                            masked_qr_codes[number][col_index][row_index] = 0
                                