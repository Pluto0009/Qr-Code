
import qrcodevariable
from PrepareQRCode import prepare_code
from fill import fillNormal

def GenerateQRCode(link: str):
    qrcodevariable.link_length = len(link)
    prepare_code()
    fillNormal(link)