from Fillorder import generate_qr_list
from  link_to_binary import link_to_binary_list
from qrcodevariable import qr_code
from gpu import erstelle_pixel_bild
from Reed_Solomon_error_correction import Error_correction_bits_erstellen





def fillNormal(link: str):
    inputbinar = link_to_binary_list(link)
    #inputbinar = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]


    max_bits = 34 * 8 # Kapazität für Version 2, Korrekturlevel L
    
    # 1. Check ob es überhaupt passt
    if len(inputbinar) > max_bits:
        print("Zu lang!")
        return False
    
    # --- PADDING LOGIK START ---
    
    # 2. Terminator hinzufügen (bis zu 4 Nullen, aber nur so viele wie Platz ist)
    terminator_bits = min(4, max_bits - len(inputbinar))
    for _ in range(terminator_bits):
        inputbinar.append(0)
        
    # 3. Auf das nächste volle Byte auffüllen (Bit-Alignment)
    while len(inputbinar) % 8 != 0 and len(inputbinar) < max_bits:
        inputbinar.append(0)
        
    # 4. Mit Padding-Bytes auffüllen (0xEC und 0x11 abwechselnd)
    padding_patterns = [
        [1, 1, 1, 0, 1, 1, 0, 0], # 0xEC (236)
        [0, 0, 0, 1, 0, 0, 0, 1]  # 0x11 (17)
    ]
    
    pattern_index = 0
    while len(inputbinar) < max_bits:
        current_pattern = padding_patterns[pattern_index % 2]
        # Sicherstellen, dass wir nicht über max_bits hinausschießen
        for bit in current_pattern:
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

    for i in range(len(error_correction_bits)):
        bits.append(error_correction_bits[i])



    for inputbytePos in range(0, len(bits)):


        for i, teil_liste in enumerate(qrFillorder):      # äußerer Index
            for j, pos in enumerate(teil_liste):          # innerer Index
                if pos == inputbytePos + 13:
                    qr_code[i][j] = bits[inputbytePos]
                    print(inputbytePos)



# print(dataANDKorrekturbits("Abc"))
# print(qr_code)
# erstelle_pixel_bild(qr_code)




                
        
        

    

