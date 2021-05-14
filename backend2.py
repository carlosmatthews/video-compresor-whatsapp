from moviepy.editor import *
import os

class ConversorVideo():
    def __init__(self,video):
        self.video = video
        
    def start(self):    
        self.video_escalado, self.ruta_salida = self.escalar_video()
        self.tamaño_archivo = os.stat(self.video_escalado).st_size / 1024 / 1024 # peso en MB
        self.tamaño_maximo = 60 # maximo en MB, luego sera seteable el base para whatsapp es 60MG
        if self.tamaño_archivo > self.tamaño_maximo:
            self.cortar_en_partes(self.ruta_salida)
            os.remove(self.video_escalado)
    
    def escalar_video(self):
        resolucion_video_out = (640,360) #tamaño para whatsapp, luego se podra setear en otros valores
        ruta_salida, nombre_salida = os.path.split(self.video)
        nombre_salida = nombre_salida.rsplit(".", 1)
        nombre_salida.insert(1, "resize")
        nombre_salida = ".".join(nombre_salida)
        ruta_salida_intermedio = os.path.join(ruta_salida, nombre_salida)
        if not os.path.exists(ruta_salida_intermedio):
            print("se va escalar el video a" f"{resolucion_video_out} espere")
            ffmpeg_tools.ffmpeg_resize(self.video, ruta_salida_intermedio, resolucion_video_out)    
        else:
            print("parece que ya escalo el video")
        return ruta_salida_intermedio, ruta_salida    
    
    def cortar_en_partes(self, ruta_salida):      
        clip = VideoFileClip(self.video_escalado) #instancia el video para cortarlo
        print ("tamaño_archivo:", self.tamaño_archivo )
        numero_de_partes = int(self.tamaño_archivo // self.tamaño_maximo + 1)
        print("se cortara en:",numero_de_partes, "partes")
        print(clip.duration)
        duracion_fragmento = int(clip.duration // numero_de_partes)
        inicio = 0
        fin = inicio + duracion_fragmento 
            
        for n in range(numero_de_partes):
            video_cortado = clip.subclip(inicio,inicio + fin)# copia y crear subclip segmentado
            nombre_video = f"{self.ruta_salida}/fragmento_{n}.mp4"
            video_cortado.write_videofile(nombre_video) # guardar cada subclip
            inicio += duracion_fragmento
        clip.close()


