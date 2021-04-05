
""" programa para partir en segmentos y comprimir videos mas largos y de mayor peso que los 64 Mg que permite Whatsapp, 
para mostrar trabajos y su visualisacion rapida.
"""
#comprescion por defecto H264,('libx264', 24 fps)

from moviepy.editor import *
import os
import sys

if len(sys.argv) > 1 :
    mi_video = sys.argv[1]
else:
    mi_video = input("ingrese la ruta del video, \n ejemplo:\n E:/03 EDICIONES PROYECTOS ABIERTOS/acto completo 15-3 HD_parte 1 A.mp4\n") #entrada por consola

if not os.path.exists(mi_video):
    print("el archivo no existe")
    exit(1)

def escalar_video(video_original):
    resolucion_video_out = (640,360) #tamaño para whatsapp, luego se podra setear
    ruta_salida, nombre_salida = os.path.split(mi_video)
    nombre_salida = nombre_salida.rsplit(".", 1)
    nombre_salida.insert(1, "resize")
    nombre_salida = ".".join(nombre_salida)
    ruta_salida_intermedio = os.path.join(ruta_salida, nombre_salida)
    if not os.path.exists(ruta_salida_intermedio):
        print("se va escalar el video a" f"{resolucion_video_out} espere")
        ffmpeg_tools.ffmpeg_resize(mi_video, ruta_salida_intermedio, resolucion_video_out)    
    else:
         print("parece que ya escalo el video")
    return ruta_salida_intermedio, ruta_salida
  
def cortar_en_partes(video_escalado, ruta_salida):      
    clip = VideoFileClip(video_escalado) #instancia el video para cortarlo
    print ("tamaño_archivo:", tamaño_archivo )
    numero_de_partes = int(tamaño_archivo // tamaño_maximo + 1)
    print("se cortara en:",numero_de_partes, "partes")
    print(clip.duration)
    duracion_fragmento = int(clip.duration // numero_de_partes)
    inicio = 0
    fin = inicio + duracion_fragmento 
        
    for n in range(numero_de_partes):
        video_cortado = clip.subclip(inicio,inicio + fin)# copia y crear subclip segmentado
        nombre_video = f"{ruta_salida}/fragmento_{n}.mp4"
        video_cortado.write_videofile(nombre_video) # guardar cada subclip
        inicio += duracion_fragmento
        

video_escalado, ruta_salida = escalar_video(mi_video)

tamaño_archivo = os.stat(video_escalado).st_size / 1024 / 1024 # peso en MB
tamaño_maximo = 42 # maximo en MB, luego sera seteable el base para whatsapp es 60MG

if tamaño_archivo > tamaño_maximo:
    cortar_en_partes(video_escalado, ruta_salida)
    os.remove(video_escalado)



