import shutil
from deepface import DeepFace
import cv2
import glob
import os
import datetime

def guardar_frames(carpeta,frame):
    print("Ejecutando guardar_frames")
    # guardar_frames recibe el nombre de una carpeta ¬°
    # y un frame de opencv y lo almacena en la ¬°
    # carpeta con un nombre basado en la hora actual.

    #Si la carpeta no exista, crea una.
    if not os.path.exists(carpeta): 
        print("Carpeta no existe, creando carpeta: " + carpeta)
        os.makedirs(carpeta)
    hora = datetime.datetime.now()
    nombre_archivo = carpeta + "/frame" + "%" + hora.strftime("%H-%M-%S") + ".jpg"
    #El nombre del archivo es la carpeta + frame + hora actual en formato H-M-S
    cv2.imwrite(nombre_archivo, frame) #imwrite guarda el frame en la carpeta (Si, parte del nombre tiene que ser la ubicacion del arhivo)
    print("Guardando frame " + nombre_archivo) #Confirmacion en la terminal de comandos lol
    return nombre_archivo


def eliminar_fotos():
    print("Ejecutando eliminar_fotos")
    carpeta_temp = os.path.join("fotos", "temp")
    fotos = glob.glob(carpeta_temp + "/*.jpg")
    #Glob basicamente busca todas las fotos dentro de la carpeta temp
    for foto in fotos:
        
        print("Procesando " + foto)
        os.remove(foto)


def activar_camara(n):
    print("Ejecutando activar_camara" + str(n))
    cap = cv2.VideoCapture(n)
    if not cap.isOpened():
        print("Error al abrir la cámara.")
        return
    contador_frames = 0
    while True:
        retorno, frame = cap.read()
        if not retorno:
            break

        contador_frames += 1
        cv2.imshow("Video", frame)
        if contador_frames % 50 == 0:
            frame_guardado = guardar_frames("fotos",frame)
        #    deteccion = DeepFace.extract_faces(frame, detector_backend="yunet", enforce_detection=False)
        #    if deteccion is None:
        #        print("No se detectó rostro en el frame.")
        #        shutil.move(frame_guardado, os.path.join("fotos", "temp", os.path.basename(frame_guardado)))
        #    else:
        #        print("Rostro detectado, guardando frame.")
        #        shutil.move(frame_guardado, os.path.join("fotos", "detecciones", os.path.basename(frame_guardado)))

            resultado = DeepFace.find(frame_guardado, db_path="data", model_name="SFace", enforce_detection=False)
            print("Resultado:", resultado[0])
            #print("Mas info de resultado:", resultado[0].iloc[0]["identity"])
            if resultado[0].empty:
                print("No se encontró coincidencias.")
                shutil.move(frame_guardado, os.path.join("fotos", "temp", os.path.basename(frame_guardado)))
                #mover_a_carpeta(frame_guardado, "fotos\temp")
            else:
                print("Reconocido:", resultado[0].iloc[0]["identity"])
                shutil.move(frame_guardado, os.path.join("fotos", "detecciones", os.path.basename(frame_guardado)))


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    print("TEST5")
    activar_camara(0)

    print("Desea elimnar las fotos guardadas? (s/n)")
    respuesta = input()
    if respuesta.lower() == 's':
        eliminar_fotos()
    else:
        print("No se eliminaron las fotos guardadas.")