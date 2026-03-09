import qrcodevariable
from Fillorder import generate_qr_list
from link_to_binary import link_to_binary_list
from gpu import erstelle_pixel_bild
from Reed_Solomon_error_correction import Error_correction_bits_erstellen

def fillNormal(link: str):
    inputbinar = []
    # Modus: Byte mode = 0100
    inputbinar += [0, 1, 0, 0]

    # Anzahl data bits (8 bits)
    length = len(link)
    for i in range(7, -1, -1):
        inputbinar.append((length >> i) & 1)

    # Data bytes
    inputbinar += link_to_binary_list(link)
    # inputbinar += [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

    max_bits = 34 * 8  # Version 2, EC Level L

    if len(inputbinar) > max_bits:
        print("Zu lang!")
        return False
    
    # --- PADDING LOGIK START ---


    # 2. Terminator hinzufügen (bis zu 4 Nullen, aber nur so viele wie Platz ist)
    for _ in range(4):
        if len(inputbinar) < max_bits:
            inputbinar.append(0)

    # 3. Auf das nächste volle Byte auffüllen (Bit-Alignment)
    while len(inputbinar) % 8 != 0:
        if len(inputbinar) < max_bits:
            inputbinar.append(0)


    # 4. Mit Padding-Bytes auffüllen (0xEC und 0x11 abwechselnd)
    padding_patterns = [
        [1,1,1,0,1,1,0,0],  # 0xEC (236)
        [0,0,0,1,0,0,0,1],  # 0x11 (17)
    ]

    pattern_index = 0
    while len(inputbinar) < max_bits:
        for bit in padding_patterns[pattern_index % 2]:
            if len(inputbinar) < max_bits:
                inputbinar.append(bit)
        pattern_index += 1

    # --- PADDING LOGIK ENDE ---

                    
    #print(type(qr_code))
    
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