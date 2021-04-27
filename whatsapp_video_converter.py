
""" programa para partir en segmentos y comprimir videos mas largos y de mayor peso que los 64 Mg que permite Whatsapp, 
para mostrar trabajos y su visualisacion rapida.
"""
#comprescion por defecto H264,('libx264', 24 fps)

from moviepy.editor import *
import os
import sys
from back_end_for_gui import start


if len(sys.argv) > 1 :
    mi_video = sys.argv[1]
else:
    mi_video = input("ingrese la ruta del video, \n ejemplo:\n E:/03 EDICIONES PROYECTOS ABIERTOS/acto completo 15-3 HD_parte 1 A.mp4\n") #entrada por consola

if not os.path.exists(mi_video):
    print("el archivo no existe")
    exit(1)

start(mi_video)