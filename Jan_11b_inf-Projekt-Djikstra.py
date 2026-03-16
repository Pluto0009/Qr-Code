import math # um math.inf zu verwenden (unendlich)

def dijkstra(graph, start):

    # Alle Distanzen auf unendlich setzen außer Start (0)
    distanzen = {knoten: math.inf for knoten in graph}
    distanzen[start] = 0
    
    # Hier merken wir uns den "Vorgänger" für den Rückweg später
    vorgaenger = {knoten: None for knoten in graph}
    
    # Liste aller Knoten die noch bearbeitet werden müssen
    unbesucht = list(graph.keys())

    # 2. DER ALGORITHMUS

    while unbesucht:
        # Wähle den unbesuchten Knoten mit der kleinsten Distanz
        aktueller_knoten = min(unbesucht, key=lambda k: distanzen[k])
        
        # Abbruch falls der Rest Distanz ist unendlich
        if distanzen[aktueller_knoten] == math.inf:
            break
            
        unbesucht.remove(aktueller_knoten)
        
        # Nachbarn prüfen.
        for nachbar, gewicht in graph[aktueller_knoten].items():
            if nachbar in unbesucht:
                neue_distanz = distanzen[aktueller_knoten] + gewicht
                
                # Wenn ein kürzerer weg gefunden wurde
                if neue_distanz < distanzen[nachbar]:
                    distanzen[nachbar] = neue_distanz
                    # Speichere woher wir kommen für backtrack
                    vorgaenger[nachbar] = aktueller_knoten
                    
    return distanzen, vorgaenger

def weg_rekonstruieren(vorgaenger, start, ziel):
    
    # WEG FINDEN
    
    
    # Wir fangen beim ziel an und gehen rückwärts bis zum Start
    pfad = []
    aktueller_schritt = ziel
    
    # Solange wir einen gültigen Knoten haben
    while aktueller_schritt is not None:
        # Knoten vorne in die Liste einfügen
        pfad.insert(0, aktueller_schritt)
        
        # Wenn wir beim Start angekommen sind==fertig
        if aktueller_schritt == start:
            break
            
        # Einen Schritt zurückgehen.
        aktueller_schritt = vorgaenger[aktueller_schritt]
        
    return pfad


# HAUPTPROGRAMM MIT EINGABE


if __name__ == "__main__":
    # Graph (Beispielstädte noch macjen !!!!!!!!!!!)
    mein_graph = {
        "ERLANGEN": {"NÜRNBERG": 17, "FÜRTH": 18},
        "NÜRNBERG": {"ERLANGEN": 17, "FÜRTH": 8, "BAMBERG": 63},
        "FÜRTH": {"ERLANGEN": 18, "NÜRNBERG": 8, "BAMBERG": 59},
        "BAMBERG": {"NÜRNBERG": 63, "FÜRTH": 59}
    }
    
    print("--- Dijkstra Routenplaner ---")
    print(f"Verfügbare Orte: {list(mein_graph.keys())}")
    
    # Nutzer nach Start und Ziel fragen
    # .strip().upper() entfernt Leerzeichen und macht alles groß (A = a)
    start_eingabe = input("Bitte Startknoten eingeben: ").strip().upper()
    ziel_eingabe = input("Bitte Zielknoten eingeben: ").strip().upper()
    

    #print((start_eingabe), (ziel_eingabe))

    # Prüfung Gibt es diese Knoten überhaupt im Graphen?
    if start_eingabe in mein_graph and ziel_eingabe in mein_graph:
        
        # 1. Algorithmus ausführen
        ergebnis_distanzen, ergebnis_vorgaenger = dijkstra(mein_graph, start_eingabe)
        
        # 2. Gesamtdistanz prüfen
        distanz = ergebnis_distanzen[ziel_eingabe]
        
        if distanz == math.inf:
            print(f"Es gibt keinen Weg von {start_eingabe} nach {ziel_eingabe}.")
        else:
            # 3. Den genauen Weg als Liste holen
            weg_liste = weg_rekonstruieren(ergebnis_vorgaenger, start_eingabe, ziel_eingabe)
            
            # 4. Ausgabe formatieren (z.B. "A -> C -> D")
            weg_string = " -> ".join(weg_liste)
            
            print("-" * 30)
            print(f"Kürzeste Route: {weg_string}")
            print(f"Gesamtdistanz:  {distanz} km")
            print("-" * 30)
            
    else:
        print("Fehler: Einer der eingegebenen Knoten existiert nicht!")