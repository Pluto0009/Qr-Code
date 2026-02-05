
import qrcodevariable
from PrepareQRCode import prepare_code
from fill import fillNormal
from gpu import erstelle_pixel_bild


def GenerateQRCode(link: str):
    qrcodevariable.link_length = len(link)
    prepare_code()
    fillNormal(link)
    erstelle_pixel_bild(qrcodevariable.qr_code)




GenerateQRCode("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567")