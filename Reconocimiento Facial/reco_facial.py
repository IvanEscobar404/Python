import cv2 ##Importamos cv2, que es una libreria que se descarga


##La variable 'face_cascade' va a tener como referencia la ubicacion de 'cascade' que se descarga
face_detector = cv2.CascadeClassifier('Reconocimiento Facial/haarcascade_frontalface_default.xml') ##Entre parentesis la ubicacion

##La variable 'cap' con 'cv2.videocapture' va a tomar nuestra webcam:
cap = cv2.VideoCapture(0) ##El 0 es un parametro, dependiendo si esta ocupada la webcam principal y tenes otra, simplemente pones el 1 o 2.


while True:
    succesful_frame_read, frame = cap.read()

    if not succesful_frame_read:
        break

    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(frame_grayscale)

    

    for (x, y, w, h) in faces:  
        cv2.rectangle(frame, (x,y), (x+w, y+h), (100, 200, 50), 2)   

    cv2.imshow('videoXD', frame) 
    k = cv2.waitKey(50) 
    if k == 27: 
        break

cap.release() 
cv2.destroyAllWindows() 

print('Funcionando')


