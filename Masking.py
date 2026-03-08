import qrcodevariable
import math

masked_qr_codes = []
mask_penalty_scores = []

def apply_masking():
    for i in range(8):
        masked_qr_codes[i] = qrcodevariable.qr_code
        mask_penalty_scores[i] = 0
        apply_mask(i)
        calculate_penalty_score(i)
    for i in range(8):
        if max(mask_penalty_scores) == mask_penalty_scores[i]:
            qrcodevariable.qr_code = masked_qr_codes[i]
        
    

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
    calculate_penalty_score_condition_3(number)
    calculate_penalty_score_condition_4(number)

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

def calculate_penalty_score_condition_3(number: int):
    pattern = []
    for i in range(3):
        pattern[i] = 0
    pattern[4] = 1
    pattern[5] = 0
    for i in range(6,8):
        pattern[i] = 1
    pattern[9] = 0
    pattern[10] = 1
    for col_index, column in enumerate(masked_qr_codes[number]):
            if col_index > 10:
                break
            for row_index, module in enumerate(column):
                if row_index > 10:
                    break

                pattern_found = []
                for i in range(3):
                    pattern_found[i] = True
                for i in range(10):
                    if masked_qr_codes[number][col_index + i][row_index] != pattern[i]:
                        pattern_found[0] = False
                    if masked_qr_codes[number][col_index + i][row_index] != pattern[10 - i]:
                        pattern_found[1] = False
                    if masked_qr_codes[number][col_index][row_index + i] != pattern[i]:
                        pattern_found[2] = False
                    if masked_qr_codes[number][col_index][row_index + i] != pattern[10 - i]:
                        pattern_found[3] = False
                for i in range(3):
                    if pattern_found[i] == True:
                        mask_penalty_scores[number] += 40
                
def calculate_penalty_score_condition_4(number: int):
          previous_multiple = 0
          next_multiple = 0
          module_amount = 0
          dark_module_amount = 0
          dark_module_percent = 0
          for col_index, column in enumerate(masked_qr_codes[number]):
            for row_index, module in enumerate(column):
                module_amount += 1
                if module == 1:
                    dark_module_amount += 1
            dark_module_percent = (dark_module_amount / module_amount) * 100
            previous_multiple = math.floor(dark_module_percent / 5) * 5
            next_multiple = math.ceil(dark_module_percent / 5) * 5
            previous_multiple = abs(previous_multiple - 50)
            next_multiple = abs(next_multiple - 50)
            previous_multiple /= 5
            next_multiple /= 5
            if previous_multiple <= next_multiple:
                mask_penalty_scores[number] += previous_multiple * 10
            else:
                mask_penalty_scores[number] += next_multiple * 10
            
                          
                
                    