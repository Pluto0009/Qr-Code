import Fillorder
import link_to_binary
import qrcodevariable



def fillNormal(link: str):
    qrFillorder = Fillorder.generate_qr_list() 
    inputbinar = link_to_binary.link_to_binary_list(link)

    if len(inputbinar) > 34*8:      # check ob es passt
        return False
    
    for inputbytePos in range(4, len(inputbinar)):


        for i, teil_liste in enumerate(qrFillorder):      # äußerer Index
            for j, pos in enumerate(teil_liste):   # innerer Index
                if pos == inputbytePos:
                    qrcodevariable.qr_code[i][j] = inputbinar[inputbytePos]
                    break
            break
        




                
        
        

    

