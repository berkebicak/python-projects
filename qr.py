import pyqrcode
from pyqrcode import QRCode

address = "https://www.github.com/berkebicak"

url = pyqrcode.create(address)

url.svg("berkeqr.svg", scale=8)
