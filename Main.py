
import qrcodevariable
import Fillorder
from PrepareQRCode import prepare_code
from fill import dataANDKorrekturbits
from gpu import erstelle_pixel_bild
from datasizeandtype import fill_data_size_and_type
from Masking import apply_masking
from FormatString import generate_format_string
from linkshortner import shorten_url


def GenerateQRCode(link: str):
    link = shorten_url(link)
    qrcodevariable.link_length = len(link)
    qrcodevariable.fill_order_grid = Fillorder.generate_qr_list()
    prepare_code()
    dataANDKorrekturbits(link)
    fill_data_size_and_type()
    apply_masking()
    generate_format_string()
    erstelle_pixel_bild(qrcodevariable.qr_code)

GenerateQRCode("www.youtube.com")



# error corektion L