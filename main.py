#from deepface import DeepFace
import cv2
import glob
import os
import datetime
cap = cv2.VideoCapture(0)
contador_frames = 0
def guardar_fotos(carpeta,frame):
    now = datetime.datetime.now()
    nombre_archivo = carpeta + "/frame" + str(contador_frames//50) + now.strftime("%H:%M:%S") + ".jpg"
    cv2.imwrite(nombre_archivo, frame)
    print("Salvando frame " + nombre_archivo)

def eliminar_fotos():
    fotos = glob.glob("temp/*.jpg")
    for foto in fotos:
        print("Procesando " + foto)
        os.remove(foto)

while True:
    retorno, frame = cap.read()
    if not retorno:
        break

    contador_frames += 1
    cv2.imshow("Video", frame)
    if contador_frames % 50 == 0:
        guardar_fotos("temp",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
