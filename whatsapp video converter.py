
""" programa para partir en segmentos y comprimir videos mas largos y de mayor peso que los 64 Mg que permite Whatsapp, 
para mostrar trabajos y su visualisacion rapida.
"""
#TODO: DETERMINAR EL RATE DE COMPRESION A USAR EN FORMATO h264  Y SU DURACION PARA PARTIR EN SEGMENTOS MENORES A 64MB
# probar peso en 720x480p@25 1000 Kb/s
#TODO: BUSCAR MODULO DE PYTHON PARA CORTAR Y COMPRIMIR VIDEO. libreria MoviePY

from moviepy.editor import *
import os

mi_video = "E:/03 EDICIONES PROYECTOS ABIERTOS/misterio de obras publicas/acto completo 15-3 HD_parte 1 A.mp4" #entrada por consola
tamaño_video_out = (640,360) #luego se podra setear
carpeta_salida_intermedio = "E:/03 EDICIONES PROYECTOS ABIERTOS/misterio de obras publicas/video_resize.mp4" #automatico igual a la de origen"""
#ffmpeg_tools.ffmpeg_resize(mi_video, carpeta_salida_intermedio, tamaño_video_out)
tamaño_archivo = os.stat(carpeta_salida_intermedio).st_size / 1024 / 1024 # peso en MB

clip = VideoFileClip(carpeta_salida_intermedio)

tamaño_maximo = 42 # maximo en MB

if tamaño_archivo > tamaño_maximo:
    print (tamaño_archivo)
    numero_de_partes = tamaño_archivo // tamaño_maximo + 1
    print(clip.duration)
    print (clip.duration // numero_de_partes)












