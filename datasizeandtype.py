
import qrcodevariable
bit_array = []

def fill_data_size_and_type():
    fill_data_type()
    fill_data_size()

# Setzt innerhalb der ersten 4 Module den Datentyp auf "Bit"

def fill_data_type():
    qrcodevariable.qr_code[23][24] = 1

def fill_data_size():
    bit_array = [0,0,0,0,0,0,0,0]
    bit_array = qrcodevariable.link_length.to_bytes(8)
    
    for printed_bit_index in range(8):
        for col_index, column in enumerate(qrcodevariable.fill_order_grid):
            for row_index, pos in enumerate(column):
                if pos == printed_bit_index:
                    qrcodevariable.qr_code[col_index][row_index] = bit_array[printed_bit_index]