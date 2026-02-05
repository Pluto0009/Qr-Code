from Fillorder import generate_qr_list
from  link_to_binary import link_to_binary_list
from qrcodevariable import qr_code
from gpu import erstelle_pixel_bild




def fillNormal(link: str):
    qrFillorder = generate_qr_list() 
    inputbinar = link_to_binary_list(link)

    if len(inputbinar) > 34*8:      # check ob es passt
        return False
    
    
    
    for inputbytePos in range(4, len(inputbinar)):


        for i, teil_liste in enumerate(qrFillorder):      # äußerer Index
            for j, pos in enumerate(teil_liste):          # innerer Index
                if pos == inputbytePos:
                    qr_code[i][j] = inputbinar[inputbytePos]
                    print(inputbytePos)
                    

    return True



"""
print(fillNormal("Abc"))
print(qr_code)
erstelle_pixel_bild(qr_code)

"""



                
        
        

    

