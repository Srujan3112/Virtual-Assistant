import qrcode
from speak_module import speak
import datetime
def qrCodeGenerator():
        speak(f"Boss enter the text/link that you want to keep in the qr code")
        input_Text_link = input("Enter the Text/Link : ")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=4,
        )
        QRfile_name = (str(datetime.datetime.now())).replace(" ","-")
        QRfile_name = QRfile_name.replace(":","-")
        QRfile_name = QRfile_name.replace(".","-")
        QRfile_name = QRfile_name+"-QR.png"
        qr.add_data(input_Text_link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(QRfile_name)
        speak(f"Boss the qr code has been generated")