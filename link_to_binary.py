
def link_to_binary(url):
    binary_list = []  # Wir starten mit einer leeren Liste
    for char in url:
        # Wir formatieren den Buchstaben als 8-Bit Binärzahl
        # und fügen ihn als einzelnes Element der Liste hinzu
        binary_list.append(format(ord(char), '08b')) 
    return binary_list

Dicklasssssss = link_to_binary("abc")
print(Dicklasssssss)