import qrcode
from PIL import Image

class CodigoQR():
    def __init__(self, data, name_archivo):
        self.data = data
        self.name_archivo = name_archivo

    def generar_qr(self):
        try:
            imagen = qrcode.make(self.data)
            name_archivo = self.name_archivo
            imagen.save(name_archivo)
            Image.open(name_archivo).show()
        except Exception as e:
            print(f"Error al generar el codigo QR: {e}")

if __name__ == "__main__":
    url = "https://www.google.com"
    name_archivo = "imagen_codigo.png"
    CodigoQR(url, name_archivo).generar_qr()

    ##Se puede seguir generando mas codigo QR con mas url.