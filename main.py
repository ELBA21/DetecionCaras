#from deepface import DeepFace
import cv2
import glob
import os
import datetime

def guardar_frames(carpeta,frame, contador_frames):
    now = datetime.datetime.now()
    nombre_archivo = carpeta + "/frame" + str(contador_frames//50) + "%" + now.strftime("%H-%M-%S") + ".jpg"
    cv2.imwrite(nombre_archivo, frame)
    print("Salvando frame " + nombre_archivo)

def eliminar_fotos():
    fotos = glob.glob("temp/*.jpg")
    for foto in fotos:
        print("Procesando " + foto)
        os.remove(foto)
def activar_camara():
    cap = cv2.VideoCapture(0)
    contador_frames = 0
    while True:
        retorno, frame = cap.read()
        if not retorno:
            break

        contador_frames += 1
        cv2.imshow("Video", frame)
        if contador_frames % 50 == 0:
            guardar_frames("temp",frame, contador_frames)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("TEST4")
    activar_camara()
    #print("Desea elimnar las fotos guardadas? (s/n)")
    #respuesta = input()
    #if respuesta.lower() == 's':
    #    eliminar_fotos()
    #else:
    #    print("No se eliminaron las fotos guardadas.")