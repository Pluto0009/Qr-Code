import qrcodevariable
from Fillorder import generate_qr_list
from link_to_binary import link_to_binary_list
from gpu import erstelle_pixel_bild
from Reed_Solomon_error_correction import Error_correction_bits_erstellen

def fillNormal(link: str):
    inputbinar = []
    # Mode Indicator: Byte mode = 0100
    inputbinar += [0, 1, 0, 0]
    # Character count (8 bits)
    length = len(link)
    for i in range(7, -1, -1):
        inputbinar.append((length >> i) & 1)
    # Data bytes
    inputbinar += link_to_binary_list(link)

    max_bits = 34 * 8  # Version 2, EC Level L

    if len(inputbinar) > max_bits:
        print("Zu lang!")
        return False

    # Terminator
    for _ in range(4):
        if len(inputbinar) < max_bits:
            inputbinar.append(0)

    # Byte alignment
    while len(inputbinar) % 8 != 0:
        if len(inputbinar) < max_bits:
            inputbinar.append(0)

    # Padding bytes 0xEC, 0x11 alternating
    padding_patterns = [
        [1,1,1,0,1,1,0,0],  # 0xEC
        [0,0,0,1,0,0,0,1],  # 0x11
    ]
    pattern_index = 0
    while len(inputbinar) < max_bits:
        for bit in padding_patterns[pattern_index % 2]:
            if len(inputbinar) < max_bits:
                inputbinar.append(bit)
        pattern_index += 1

    return inputbinar

def dataANDKorrekturbits(link: str):
    qrFillorder = generate_qr_list()
    bits = fillNormal(link)
    error_correction_bits = Error_correction_bits_erstellen(bits)
    for b in error_correction_bits:
        bits.append(b)

    for inputbytePos in range(len(bits)):
        for i, teil_liste in enumerate(qrFillorder):
            for j, pos in enumerate(teil_liste):
                if pos == inputbytePos + 1:
                    qrcodevariable.qr_code[i][j] = bits[inputbytePos]