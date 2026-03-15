import goliathfieldmathematik as gf
import math

# Von Leopold

def bitsTOint(bits: list[int]):
    bits_reversed = bits[::-1]
    val = sum(bit * (2**i) for i, bit in enumerate(bits_reversed))
    return val


def intTObits(number: int):
    bit_list = [(number >> i) & 1 for i in range(7, -1, -1)]
    return bit_list

def Error_correction_bits_erstellen(daten: list[int]):

    if (len(daten) % 8) != 0:
        print("Fuck")
        return False


    intList = []
    for i in range(len(daten)//8):
        intList.append(bitsTOint(daten[i*8:(i+1)*8]))


    generator_polynomial = [1, 216, 194, 159, 111, 199, 94, 95, 113, 157, 193]

    register = []

    register = intList.copy()
    for i in range(10):
        register.append(0)

    


    while(len(register) > 10):
        if register[0] == 0:
            register.pop(0)
        else:
            hilfs_list = []
            for i2 in range(len(generator_polynomial)):
                hilfs_list.append(bitsTOint(gf.mulitplizierenGF(intTObits(register[0]), intTObits(generator_polynomial[i2]))))
            
            for i in range(len(hilfs_list)):
                register[i] = bitsTOint(gf.addierenGF(intTObits(register[i]), intTObits(hilfs_list[i])))
            
            register.pop(0)
    


    finallist = []

    for i in range(len(register)):
        bitList = intTObits(register[i])
        for i2 in range(len(bitList)):
            finallist.append(bitList[i2])
      

    return finallist

            