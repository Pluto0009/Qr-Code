
import qrcodevariable
from PrepareQRCode import prepare_code
from fill import fillNormal
from gpu import erstelle_pixel_bild
from datasizeandtype import fill_data_size_and_type


def GenerateQRCode(link: str):
    qrcodevariable.link_length = len(link)
    prepare_code()
    fillNormal(link)
    fill_data_size_and_type()
    erstelle_pixel_bild(qrcodevariable.qr_code)

GenerateQRCode("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567")