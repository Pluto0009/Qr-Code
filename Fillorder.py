def generate_qr_list():
    size = 25

    
    # Erstellt eine 25x25 Matrix gefüllt mit Nullen
    qr = [[0 for _ in range(size)] for _ in range(size)]
    
    # Maske erstellen: True bedeutet "besetzt durch System-Muster"
    mask = [[False for _ in range(size)] for _ in range(size)]
    
    # 1. Finder Patterns (die großen Quadrate + Margin)
    for r in range(size):
        for c in range(size):
            if (r < 9 and c < 9) or (r < 9 and c > 16) or (r > 16 and c < 9):
                mask[r][c] = True
    
    # 2. Alignment Pattern (das kleine Quadrat unten rechts)
    for r in range(16, 21):
        for c in range(16, 21):
            mask[r][c] = True
            
    # 3. Timing Lines (die gepunkteten Linien bei Index 6)
    for i in range(size):
        mask[6][i] = True
        mask[i][6] = True

    # Zick-Zack Pfad ablaufen (Start rechts unten)
    current_val = 1
    column = size - 1
    upwards = True
    
    while column > 0:
        # Die vertikale Timing-Line bei Spalte 6 wird übersprungen
        if column == 6:
            column -= 1
            
        # Zeilenbereich festlegen (von unten nach oben oder oben nach unten)
        rows = range(size - 1, -1, -1) if upwards else range(size)
        
        for r in rows:
            # In jeder 2er-Spalte: erst rechts, dann links
            for c in (column, column - 1):
                if not mask[r][c]:
                    qr[r][c] = current_val
                    current_val += 1
        
        upwards = not upwards  # Richtung wechseln
        column -= 2


       
    
        
    #flip
    qrflip = [[0 for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            qrflip[x][y] = qr[y][x]

    return qrflip


print(generate_qr_list())