import qrcodevariable

format_string = []
error_correction = []
generator_poly = []
final_format_string = []

def generate_format_string():
    global format_string, generator_poly, error_correction, final_format_string
    
    # Reset globals to allow multiple calls
    format_string = []
    error_correction = []
    generator_poly = []
    final_format_string = []
    
    # EC level L = 01, mask in 3 bits
    format_string = [0, 1, 0, 0, 0]
    format_string[2] = (qrcodevariable.used_mask >> 2) & 1
    format_string[3] = (qrcodevariable.used_mask >> 1) & 1
    format_string[4] = (qrcodevariable.used_mask >> 0) & 1
    
    # FIXED: Correct QR format info generator polynomial = 10100110111
    generator_poly = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1]
    
    # Compute remainder: format_string * x^10 div generator
    error_correction = format_string[:] + [0] * 10
    
    while len(error_correction) > 10:
        error_correction = binary_division(error_correction, generator_poly)
    
    if len(error_correction) < 10:
        error_correction = [0] * (10 - len(error_correction)) + error_correction
    
    final_format_string = format_string[:] + error_correction[:]
    
    # XOR with mask 101010000010010
    final_mask = [1,0,1,0,1,0,0,0,0,0,1,0,0,1,0]
    for i in range(15):
        final_format_string[i] ^= final_mask[i]
    
    paste_formate_string(final_format_string)

def binary_division(_error_correction, _generator_poly):
    # Work on copies to avoid mutation
    ec = _error_correction[:]
    
    # Strip leading zeros
    while ec and ec[0] == 0:
        ec.pop(0)
    
    if len(ec) <= 10:
        return ec
    
    # Align generator to same length
    gen = _generator_poly[:]  # FIXED: use fresh copy, don't mutate original
    while len(gen) < len(ec):
        gen.append(0)
    
    # XOR
    for i in range(len(ec)):
        ec[i] ^= gen[i]
    
    # Strip leading zeros
    while ec and ec[0] == 0:
        ec.pop(0)
    
    return ec

def paste_formate_string(_final_format_string):
    # --- TOP-LEFT finder pattern area ---
    # Horizontal (col=8 fixed, rows 0-5)
    for i in range(6):
        qrcodevariable.qr_code[8][i] = _final_format_string[i]
    # Skip timing line at row 6, bit 6 goes to row 7
    qrcodevariable.qr_code[8][7] = _final_format_string[6]
    # Corner: col=8, row=8
    qrcodevariable.qr_code[8][8] = _final_format_string[7]
    # Vertical (row=8 fixed, cols 7,5,4,3,2,1,0) -- skip col 6 (timing)
    qrcodevariable.qr_code[7][8] = _final_format_string[8]
    for i in range(6):
        qrcodevariable.qr_code[5 - i][8] = _final_format_string[9 + i]

    # --- BOTTOM-LEFT copy (col=8 fixed, rows 24 down to 18) ---
    # bits 0-6 go here
    for i in range(7):
        qrcodevariable.qr_code[8][24 - i] = _final_format_string[i]

    # --- TOP-RIGHT copy (row=8 fixed, cols 17-24) ---
    # bits 7-14 go here (bit 7 at col 17, bit 14 at col 24)
    for i in range(8):
        qrcodevariable.qr_code[17 + i][8] = _final_format_string[7 + i]