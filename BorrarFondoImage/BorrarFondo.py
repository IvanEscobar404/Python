from rembg import remove
from PIL import Image

# Cargar la imagen
imagen_con_fondo = Image.open("BorrarFondoImage/messi.jpg") 

# Eliminar el fondo
imagen_sinfondo = remove(imagen_con_fondo)

# Guardar la imagen sin fondo
imagen_sinfondo.save("imagenSinfondo.png")
print("Fondo eliminado correctamente")