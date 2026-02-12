import qrcodevariable
import math

masked_qr_codes = []
mask_penalty_scores = []

def apply_masking():
    for i in range(8):
        masked_qr_codes[i] = qrcodevariable.qr_code
        mask_penalty_scores[i] = 0
        apply_mask(i)
    

def apply_mask(number: int):
    
    for col_index, column in enumerate(qrcodevariable.fill_order_grid):
            for row_index, pos in enumerate(column):
                if pos != 0:
                    mask_result = -1
                    match number:
                        case 0:
                            mask_result = math.fmod(row_index + col_index, 2)
                        case 1:
                            mask_result = math.fmod(row_index, 2)
                        case 2:
                            mask_result = math.fmod(col_index, 3)
                        case 3:
                            mask_result  = math.fmod(row_index + col_index, 3)
                        case 4:
                            mask_result = math.fmod(math.floor(row_index / 2) + math.floor(col_index / 3), 2)
                        case 5:
                            mask_result  = math.fmod(row_index * col_index, 2) + math.fmod(row_index * col_index, 3)
                        case 6:
                            mask_result = math.fmod(math.fmod(row_index * col_index, 2) + math.fmod(row_index * col_index, 3), 2)
                        case 7:
                            mask_result = math.fmod(math.fmod(row_index + col_index, 2) + math.fmod(row_index * col_index, 3), 2)
                    
                    if mask_result == 0:
                        if masked_qr_codes[number][col_index][row_index] == 0:
                            masked_qr_codes[number][col_index][row_index] = 1
                        else:
                            masked_qr_codes[number][col_index][row_index] = 0   
                                
def calculate_penalty_score(number: int):
    calculate_penalty_score_condition_1(number)
    calculate_penalty_score_condition_2(number)

def calculate_penalty_score_condition_1(number: int):
    color_streak = 0
    swapped_masked_qr_code = None
    
    for col_index, column in enumerate(masked_qr_codes[number]):
            for row_index, module in enumerate(column):
                if row_index == 0:
                    color_streak = 0
                    
                if module == 0:
                    if color_streak <= 0:
                        color_streak -= 1
                    else:
                        color_streak = -1
                else:
                    if color_streak >= 0:
                        color_streak += 1
                    else:
                        color_streak = 1
                
                if math.fabs(color_streak) == 5:
                    mask_penalty_scores[number] += 3
                elif(math.fabs(color_streak) > 5):
                    mask_penalty_scores += 1
    
    color_streak = 0
    
    for col_index, column in enumerate(masked_qr_codes[number]):
            for row_index, module in enumerate(column):
                swapped_masked_qr_code[row_index][col_index] = masked_qr_codes[number][col_index][row_index]
    
    for col_index, column in enumerate(swapped_masked_qr_code):
            for row_index, module in enumerate(column):
                if row_index == 0:
                    color_streak = 0
                    
                if module == 0:
                    if color_streak <= 0:
                        color_streak -= 1
                    else:
                        color_streak = -1
                else:
                    if color_streak >= 0:
                        color_streak += 1
                    else:
                        color_streak = 1
                
                if math.fabs(color_streak) == 5:
                    mask_penalty_scores[number] += 3
                elif(math.fabs(color_streak) > 5):
                    mask_penalty_scores += 1
                    
def calculate_penalty_score_condition_2(number: int):
    for col_index, column in enumerate(masked_qr_codes[number]):
            for row_index, module in enumerate(column):
                if row_index != 25 or col_index != 25:
                    if masked_qr_codes[number][col_index][row_index] == masked_qr_codes[number][col_index + 1][row_index]:
                        if masked_qr_codes[number][col_index + 1][row_index] == masked_qr_codes[number][col_index + 1][row_index + 1]:
                            if masked_qr_codes[number][col_index + 1][row_index + 1] == masked_qr_codes[number][col_index][row_index + 1]:
                                mask_penalty_scores[number] += 3