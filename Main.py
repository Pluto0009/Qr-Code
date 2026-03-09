import qrcodevariable
import Fillorder
from PrepareQRCode import prepare_code
from fill import dataANDKorrekturbits
from gpu import erstelle_pixel_bild
from Masking import apply_masking
from FormatString import generate_format_string
from linkshortner import shorten_url


def GenerateQRCode(link: str):
    for i in range(qrcodevariable.rows):
        for j in range(qrcodevariable.cols):
            qrcodevariable.qr_code[i][j] = 0


    link = shorten_url(link)

    qrcodevariable.link_length = len(link)
    qrcodevariable.fill_order_grid = Fillorder.generate_qr_list()
    qrcodevariable.masked_qr_codes = [[[0 for _ in range(qrcodevariable.cols)] for _ in range(qrcodevariable.rows)] for _ in range(8)]
    
    prepare_code()
    dataANDKorrekturbits(link)
    apply_masking()
    generate_format_string()
    erstelle_pixel_bild(qrcodevariable.qr_code)

GenerateQRCode("https://www.youtube.com/watch?v=dQw4w9WgXcQ")