import qrcodevariable
import math

masked_qr_codes = []
mask_penalty_scores = []

def apply_masking():
    global masked_qr_codes
    global mask_penalty_scores
    for i in range(7): 
        masked_qr_codes.append(None)
        mask_penalty_scores.append(0)
        cols,rows = 25,25
        masked_qr_codes[i] = [[0 for _ in range(cols)] for _ in range(rows)]
        for col_index, column in enumerate(masked_qr_codes[i]):
                for row_index, module in enumerate(column):
                    masked_qr_codes[i][col_index][row_index] = qrcodevariable.qr_code[col_index][row_index]
        mask_penalty_scores[i] = 0
        apply_mask(i)
        calculate_penalty_score(i)
    for i in range(7):
        if min(mask_penalty_scores) == mask_penalty_scores[i]:
            for col_index, column in enumerate(masked_qr_codes[i]):
                for row_index, module in enumerate(column):
                    qrcodevariable.qr_code[col_index][row_index] = masked_qr_codes[i][col_index][row_index]
                    
            qrcodevariable.used_mask = i
        

def apply_mask(number: int):
    global masked_qr_codes
    global mask_penalty_scores
    
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
    rows,cols = 25,25
    swapped_masked_qr_code = [[0 for _ in range(cols)] for _ in range(rows)]
    global masked_qr_codes
    global mask_penalty_scores
    
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
                    mask_penalty_scores[number] += 1
    
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
                    mask_penalty_scores[number] += 1
                    
def calculate_penalty_score_condition_2(number: int):
    global masked_qr_codes
    global mask_penalty_scores
    for col_index, column in enumerate(masked_qr_codes[number]):
            for row_index, module in enumerate(column):
                if row_index < 24 and col_index < 24:
                    if masked_qr_codes[number][col_index][row_index] == masked_qr_codes[number][col_index + 1][row_index]:
                        if masked_qr_codes[number][col_index + 1][row_index] == masked_qr_codes[number][col_index + 1][row_index + 1]:
                            if masked_qr_codes[number][col_index + 1][row_index + 1] == masked_qr_codes[number][col_index][row_index + 1]:
                                mask_penalty_scores[number] += 3

def calculate_penalty_score_condition_3(number: int):
    global masked_qr_codes
    global mask_penalty_scores
    pattern = []
    for i in range(4):
        pattern.append(0)
    pattern.append(1)
    pattern.append(0)
    for i in range(3):
        pattern.append(1)
    pattern.append(0)
    pattern.append(1)
    for col_index, column in enumerate(masked_qr_codes[number]):
            if col_index > 10:
                break
            for row_index, module in enumerate(column):
                if row_index > 10:
                    break

                pattern_found = []
                for i in range(4):
                    pattern_found.append(True)
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
          global masked_qr_codes
          global mask_penalty_scores
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
            
                          
                
                    