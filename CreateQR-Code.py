
import gpu

rows, cols = 25, 25
qr_code = [[0 for _ in range(cols)] for _ in range(rows)]

# Bereitet den blanken QR-Code vor, indem die Positionsquares, das Alignmentpattern und die Timingpatterns erstellt werden.

def prepare_code():
    create_position_square(0,0)
    create_position_square(18,0)
    create_position_square(0,18)
    create_alignment_pattern(16,16)
    create_timing_patterns()
    qr_code[8][17] = 1

# Erstellt ein Positionsquare, welcher in den Ecken des QR-Codes platziert wird. Positionsquares dienen der Orientierung des Scanners und ermöglichen es ihm, den QR-Code korrekt zu lesen, unabhängig von seiner Ausrichtung.

def create_position_square(x_start_pos: int, y_start_pos: int):
    for i in range(7):
        qr_code[x_start_pos + i][y_start_pos] = 1
        qr_code[x_start_pos + i][y_start_pos + 6] = 1
    for i in range(5):
        qr_code[x_start_pos][y_start_pos + 1 + i] = 1
        qr_code[x_start_pos + 6][y_start_pos + 1 + i] = 1
    for o in range(3):
        for i in range(3):
            qr_code[x_start_pos + 2 + i][y_start_pos + 2 + o] = 1

# Erstellt ein Alignmentpattern, welches in der Nähe der unteren rechten Ecke des QR-Codes platziert wird. Das Alignmentpattern dient dazu, die Verzerrung des QR-Codes zu korrigieren, wenn er aus einem schiefen Winkel gescannt wird.

def create_alignment_pattern(x_start_pos: int, y_start_pos: int):
    for i in range(5):
        qr_code[x_start_pos + i][y_start_pos] = 1
        qr_code[x_start_pos + i][y_start_pos + 4] = 1
    for i in range(3):
        qr_code[x_start_pos][y_start_pos + 1 + i] = 1
        qr_code[x_start_pos + 4][y_start_pos + 1 + i] = 1
    qr_code[x_start_pos + 2][y_start_pos + 2] = 1
    
# Erstellt die Timingpatterns, welche sich zwischen den Positionsquares befinden. Timingpatterns bestehen aus abwechselnden schwarzen und weißen Modulen und helfen dem Scanner, die Größe der Module zu bestimmen und die Position der Daten im QR-Code zu erkennen.

def create_timing_patterns():
    for i in range(8, 17):
        if i % 2 == 0:
            qr_code[6][i] = 1
            qr_code[i][6] = 1

# Testabschnitt

prepare_code()
gpu.erstelle_pixel_bild(qr_code)
        