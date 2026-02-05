from PIL import Image

def erstelle_pixel_bild(pixel_daten, dateiname="output.png"):
    """
    Erstellt eine Bilddatei basierend auf einer Matrix und öffnet diese.

    ### Parameter:
    - **pixel_daten** (`list[list[int]]`): 
        Ein 2D-Array (Standard: 25x25), das die Bildpunkte definiert.
        - `1`: Erzeugt einen **schwarzen** Pixel.
        - `0`: Erzeugt einen **weißen** Pixel.
    - **dateiname** (`str`, optional): 
        Der Name oder Pfad der Datei. Standardmäßig `"output.png"`.

    ### Funktionsweise:
    Die Methode interpretiert die erste Dimension des Arrays als **Breite (x)** und 
    die zweite Dimension als **Höhe (y)**. Bei ungültigen Werten (ungleich 0 oder 1) 
    wird der Vorgang abgebrochen.

    ### Rückgabewert:
    - `True`: Bild wurde erfolgreich erstellt, gespeichert und geöffnet.
    - `False`: Ein Fehler ist aufgetreten (z. B. ungültige Datenwerte).
    """

    # array[x][y] -> x ist Breite, y ist Höhe
    breite = len(pixel_daten)
    hoehe = len(pixel_daten[0])
    
    # Ein neues Bild im Modus 'L' (Luminance / Graustufen) erstellen
    # '1' für Schwarzweiß wäre auch möglich, 'L' ist oft kompatibler
    bild = Image.new('L', (breite+2, hoehe+2))

    #alles weiß
    for x in range(breite + 2):
        for y in range(hoehe + 2):
            bild.putpixel((x, y), 255)

   

    
    for x in range(breite):
        for y in range(hoehe):
            # 0 -> Weiß (255), 1 -> Schwarz (0)
            if (pixel_daten[x][y] == 1):
                farbe = 0
            elif (pixel_daten[x][y] == 0):
                farbe = 255
            else:
                print("Arrrrrrrrrrr Fuckkkkkkkkkkkkkkkkkkkk !!!!!!!!!!!!!!!!!!!!")
                return False
            
            bild.putpixel((x+1, y+1), farbe)


    

    
    # Das Bild speichern und anzeigen
    bild.save(dateiname)
    #bild.show(dateiname)
    print(f"Bild wurde als {dateiname} gespeichert.")
    return True


"""
test_array = [[0 for _ in range(25)] for _ in range(25)]
for i in range(25):
    test_array[i][12] = 1 # Horizontale Linie
    test_array[12][i] = 1 # Vertikale Linie

test_array[24][0] = 0


erstelle_pixel_bild(test_array)

"""