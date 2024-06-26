        ### MOSTRAMOS EL LINK EN CONSOLA ###
# import cv2
# import numpy as np

# capture = cv2.VideoCapture(0) ##abrimos la webcam

# while(capture.isOpened()): ##para ir capturando frame a frame
#     ret, frame = capture.read()
#     if not ret:
#         break

#     # if (cv2.waitKey(1) == ord('s')): ##si presionamos la 's' salimos del programa
#         # break
#     cv2.imshow('webCam', frame) 
#     k = cv2.waitKey(50) 
#     if k == 27: 
#         break
#     qrDetector = cv2.QRCodeDetector() ##detector de qr
#     data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame) ##nos devuelve 3 datos,data, bbox, rectified

#     if len(data) > 0:
#         print(f'Dato: {data}')
#         ##Mostramo lo Escaneado, osea el LINK
#         cv2.putText(rectifiedImage, data, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)
#         cv2.imshow('webCam', rectifiedImage)
#     else: 
#         cv2.imshow('webCam', frame)

# capture.release()
# cv2.destroyAllWindows()


        ### MOSTRAMOS EL LINK EN PANTALLA ###
# import cv2
# import numpy as np

# capture = cv2.VideoCapture(0)  # Abrimos la webcam

# while capture.isOpened():  # Para ir capturando frame a frame
#     ret, frame = capture.read()
#     if not ret:
#         break

#     cv2.imshow('webCam', frame)
#     k = cv2.waitKey(50)
#     if k == 27:
#         break

#     qrDetector = cv2.QRCodeDetector()  # Detector de QR
#     data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)  # Nos devuelve 3 datos: data, bbox, rectified

#     if len(data) > 0:
#         # Apagamos la cámara
#         capture.release()
#         cv2.destroyAllWindows()

#         # Mostramos el enlace escaneado en una ventana gráfica
#         result_img = np.ones((200, 500, 3), np.uint8) * 255  # Crear una imagen blanca
#         cv2.putText(result_img, 'Link:', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)  # Texto en negro
#         cv2.putText(result_img, data, (80, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)  # Enlace en azul
#         while True:
#             cv2.imshow('Result', result_img)
#             if cv2.waitKey(1) & 0xFF == 27:  # Presiona 'ESC' para cerrar la ventana
#                 break
#         cv2.destroyAllWindows()
#         break

# capture.release()
# cv2.destroyAllWindows()




        ### MOSTRAMOS EL LINK Y PODEMOS ACCEDER A EL ###
import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
import webbrowser

def open_link(url):  ##Funcion que abre el enlace en el navegador predeterminado
    webbrowser.open_new(url)

def show_result(link):
    # Crear la ventana principal de tkinter
    root = tk.Tk()
    root.title("QR Code Link")

    # Etiqueta con el texto "Link:" en negro
    link_label = tk.Label(root, text="Link:", font=("Helvetica", 16))
    link_label.pack(pady=10)

    # Etiqueta con el enlace en azul y subrayado, que es clickeable
    link_url = tk.Label(root, text=link, font=("Helvetica", 16), fg="blue", cursor="hand2")
    link_url.pack(pady=10)
    link_url.bind("<Button-1>", lambda e: open_link(link))

    # Mostrar la ventana
    root.mainloop()

# Abrimos la webcam
capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    cv2.imshow('webCam', frame)
    k = cv2.waitKey(50)
    if k == 27:
        break

    qrDetector = cv2.QRCodeDetector()
    data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)

    if len(data) > 0:
        capture.release()
        cv2.destroyAllWindows()
        show_result(data)
        break

capture.release()
cv2.destroyAllWindows()
