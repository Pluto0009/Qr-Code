




def addirenGF_normal(a: int, b: int):
    
    abit = format(a, '08b')
    bbit = format(b, '08b')
    c = []

    for i in range(8):
        if (abit[i] == bbit[i]):
            c.append(0)
        elif (abit[i] != bbit[i]):
            c.append(1)
    return c 

def addierenGF(a: list[int], b:list[int]):
    c = []

    for i in range(8):
        if (a[i] == b[i]):
            c.append(0)
        elif (a[i] != b[i]):
            c.append(1)
        
    return c 


def ist_gerade(n):
    if n == 0:
        return True
    return n % 2 == 0

def mulitplizierenGF(a: list[int], b:list[int]):
    a.reverse()
    b.reverse()
    
    if len(a) != 8 or len(b) != 8:
        return False
    
    multi = []

    for i in range(8):
        if a[i] == 1:
            for i2 in range(8):
                if b[i2] == 1:
                    
                    if i == 0 and i2 == 0:
                        multi.append(0)
                    elif i != 0 and i2 == 0:
                        multi.append(i)
                    elif i == 0 and i2 != 0:
                        multi.append(i2)
                    else:
                        multi.append(i + i2)
                    

    #print(f"muliti: {multi}")
    
    for i in range(14):
        if ist_gerade(multi.count(i)): # im golai fielt ist x^2 + x^2 = 0
            for i2 in range(multi.count(i)):
                multi.remove(i)
        else:
            for i2 in range(multi.count(i) - 1):
                multi.remove(i)

    s = []
    if len(multi) == 0:
        return [0,0,0,0,0,0,0,0]
    
    #--------------- VIEL ZUGROß ---------------------------------
    if max(multi) > 14:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA FUCK")
    

    
    #--------------- passend -------------------------------------
    if max(multi) < 8:
        done = False
        for i in range(8):
            for i2 in range(len(multi)):
                if i == multi[i2]:
                    s.append(1)
                    done = True
            if done == False:
                s.append(0)
            done = False
       
        
    
    #--------------- ZUGRÖß --------------------------------------
    if max(multi) >= 8:
        s = [0] * (max(multi) + 1)

        for i in range(len(multi)):
            s[multi[i]] = 1
        
        

        while True:
            if (len(s) <= 8):
                #print("break")
                break
            elif len(s) > 8 and s[-1] == 0:
                s.pop(-1)
                #print(f"s: {s}")
            else:   
                shift = len(s) - 9
                #print(f"shift: {shift}")
            

                #ist der ersatz für den höchsten wert (ist quwasie der null funktion)
                replacement = [0, 2, 3, 4]

                for i2 in range(len(replacement)):
                    replacement[i2] += shift


                s.pop(-1)
                #print(f"s: {s}")
                
                
                
                # replacement mit XOR hinzufügen
                for i2 in range(len(replacement)):
                    #print(f"replacement[i2]: {replacement[i2]}")
                    #print(f"s: {s}")
                    if s[replacement[i2]] == 1:
                        s[replacement[i2]] = 0
                    else:
                        s[replacement[i2]] = 1

        


    s.reverse()
    return s

    
# --- TESTS FÜR addierenGF (Bitweise XOR Logik) ---
# print(addierenGF([0,0,0,0,0,1,0,1], [0,0,0,0,0,0,1,1])) # Erwartet: [0,0,0,0,0,1,1,0] (5 ^ 3 = 6)
# print(addierenGF([1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1])) # Erwartet: [0,0,0,0,0,0,0,0] (255 ^ 255 = 0)
# print(addierenGF([1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1])) # Erwartet: [1,1,1,1,1,1,1,1] (170 ^ 85 = 255)
# print(addierenGF([0,0,0,0,1,0,0,0], [0,0,0,0,0,0,0,0])) # Erwartet: [0,0,0,0,1,0,0,0] (8 ^ 0 = 8)

# --- TESTS FÜR multiplizierenGF (Galois Field Multiplikation) ---
# print("Einfache Tests ohne Überlauf")

# print(mulitplizierenGF([0,0,0,0,1,0,1,0], [0,0,0,0,0,0,1,1])) # Erwartet: [0,0,0,1,1,1,1,0] (10 * 3 = 30)
# print(mulitplizierenGF([0,0,0,0,0,1,0,1], [0,0,0,0,0,1,0,0])) # Erwartet: [0,0,0,1,0,1,0,0] (5 * 4 = 20)

# print("Tests mit Überlauf (Stutzen bei x^8)")
                                                                        # Lösung ist falsch, da gemini scheiße ist im gf(256) zurechnen
# print(mulitplizierenGF([1,0,0,0,0,0,0,0], [0,0,0,0,0,0,1,0])) # Erwartet: [0,0,0,1,1,1,0,1] (128 * 2 = 29)
# print(mulitplizierenGF([0,1,0,0,0,0,0,0], [0,0,0,0,0,1,0,0])) # Erwartet: [0,0,1,1,1,0,1,0] (64 * 4 = 58)
# print(mulitplizierenGF([1,0,0,0,0,0,0,0], [0,0,0,0,0,1,0,0])) # Erwartet: [0,0,1,1,1,0,1,0] (128 * 4 = 58)
# print(mulitplizierenGF([1,1,1,1,1,1,1,1], [0,0,0,0,0,0,1,0])) # Erwartet: [1,1,1,0,0,0,1,1] (255 * 2 = 227)
# print(mulitplizierenGF([1,0,1,0,1,0,1,0], [0,0,0,0,1,0,0,0])) # Erwartet: [0,1,1,1,0,1,1,1] (170 * 8 = 119)
# print(mulitplizierenGF([0,0,0,0,0,1,1,1], [0,0,0,0,0,0,1,1])) # Erwartet: [0,0,0,0,1,0,0,1] (7 * 3 = 9)
# print(mulitplizierenGF([0,0,0,1,0,0,0,0], [0,0,0,1,0,0,0,0])) # Erwartet: [0,0,1,1,0,1,1,1] (16 * 16 = 55)
# print(mulitplizierenGF([0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])) # Erwartet: [0,0,0,0,0,0,0,0] (0 * 255 = 0)                    
            

