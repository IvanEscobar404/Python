import cv2
import numpy as np

capture = cv2.VideoCapture(0) ##abrimos la webcam

while(capture.isOpened()): ##para ir capturando frame a frame
    ret, frame = capture.read()

    if (cv2.waitKey(1) == ord('s')): ##si presionamos la 's' salimos del programa
        break
    qrDetector = cv2.QRCodeDetector() ##detector de qr
    data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame) ##nos devuelve 3 datos,data, bbox, rectified

    if len(data) > 0:
        print(f'Dato: {data}')
        cv2.imshow('webCam', rectifiedImage)
    else: 
        cv2.imshow('webCam', frame)

capture.release()
cv2.destroyAllWindows()