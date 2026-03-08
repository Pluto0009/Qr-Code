import qrcodevariable

format_string = []
error_correction = []
generator_poly = []
final_format_string = []

def generate_format_string():
    global format_string
    global generator_poly
    global error_correction
    global final_format_string
    for i in range(11):
        generator_poly.append(-1)
    for i in range(5):
        format_string.append(-1)
    format_string[0] = 0
    format_string[1] = 1
    format_string[2] = qrcodevariable.used_mask.to_bytes(3)[0]
    format_string[3] = qrcodevariable.used_mask.to_bytes(3)[1]
    format_string[4] = qrcodevariable.used_mask.to_bytes(3)[2]
    generator_poly[0] = 1
    generator_poly[1] = 0
    generator_poly[2] = 1
    generator_poly[3] = 0 
    generator_poly[4] = 0
    generator_poly[5] = 1
    generator_poly[6] = 1
    generator_poly[7] = 0
    generator_poly[8] = 1
    generator_poly[9] = 1
    generator_poly[10] = 1
    for i in range(len(format_string)):
        error_correction.append(format_string[i])
    for i in range(10):
        error_correction.append(0)
    while len(error_correction) > 10:
        error_correction = binary_division(error_correction, generator_poly)
    if len(error_correction) < 10:
        for i in range(10 - len(error_correction)):
            error_correction.insert(0,0)
    for i in range(len(format_string)):
        final_format_string.append(format_string[i])
    for i in range(len(error_correction)):
        final_format_string.append(error_correction[i])
    final_mask = []
    for i in range(15):
        final_mask.append(-1)
    final_mask[0] = 1
    final_mask[1] = 0
    final_mask[2] = 1
    final_mask[3] = 0
    final_mask[4] = 1
    final_mask[5] = 0
    final_mask[6] = 0
    final_mask[7] = 0
    final_mask[8] = 0
    final_mask[9] = 0
    final_mask[10] = 1
    final_mask[11] = 0
    final_mask[12] = 0
    final_mask[13] = 1
    final_mask[14] = 0
    for i in range(len(final_format_string)):
        final_format_string[i] = final_format_string[i] ^ final_mask[i]
    paste_formate_string(final_format_string)
        
        
def binary_division(_error_correction, _generator_poly):
    for i in range(14 - len(_error_correction)):
        _error_correction.append(0)
    for i in range(len(_error_correction)):
        if _error_correction[i] == 0:
            _error_correction.pop(i)
        else:
            break
    for i in range(len(_error_correction) - len(_generator_poly)):
        _generator_poly.append(0)
    for i in range(len(_error_correction)):
        _error_correction[i] = _generator_poly[i] ^ _error_correction[i]
    for i in range(len(_error_correction)):
        if _error_correction[i] == 0:
            _error_correction.pop(i)
        else:
            break
    return _error_correction
    
def paste_formate_string(_final_format_string):
    for i in range(5):
        qrcodevariable.qr_code[i][8]  = _final_format_string[i]
    qrcodevariable.qr_code[7][8] = final_format_string[6]
    for i in range(1):
        qrcodevariable.qr_code[8][8 - i] = final_format_string[7 + i]
    for i in range(5):
        qrcodevariable.qr_code[8][5 - i]  = _final_format_string[9 + i]
    for i in range(6):
        qrcodevariable.qr_code[8][20 - i]  = _final_format_string[i]
    for i in range(7,14):
        qrcodevariable.qr_code[i + 6][8] = _final_format_string[i]
    
    
    