import qrcode
from PIL import Image


# img = qrcode.make("https://t.me/nekbin")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data('https://t.me/nekbin')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

img.save("sample.png")
