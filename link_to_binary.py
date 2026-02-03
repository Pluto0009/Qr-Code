

def link_to_binary(url):
    binary_string = ''  # Leer starten, ohne Leerzeichen
    for char in url:
        # Wir formatieren den Buchstaben und hängen ihn direkt hinten an
        binary_string += format(ord(char), '08b') 
    return binary_string



print(link_to_binary("https://www.google.de/"))