from tkinter import*
from tkinter import filedialog
from backend import*
import threading
import multiprocessing

class VideoConverterGUI():
 
    def __init__(self):
        self.window = Tk()
        self.window.title("video compresor whatsapp")
        self.window.geometry("300x200")
        self.boton1 = Button(text ="select video",bg="pale green", command = self.open_file, font = ("Arial Bold", 12))
        self.boton1.pack(padx=10, pady=10)
        self.boton2 = Button(text ="    convert    ", bg = "pale green", command = self.crear_proceso, font = ("Arial Bold", 12))
        self.boton2.pack(padx=10, pady=10)
        self.boton3 = Button(text ="      stop       ", bg = "pale green", command = self.terminar_proceso, font = ("Arial Bold", 12))
        self.boton3.pack(padx=10, pady=10)
        self.window.mainloop()
                      
    def open_file(self):
        self.mi_video = filedialog.askopenfilename(initialdir = "/",title = "selecione video")

    
   
      
    def crear_proceso(self):
        def llamando_a_start(self):
            start(self.mi_video)    
        
        self.proceso1 = multiprocessing.Process(target = llamando_a_start) #crea un hilo(objeto) para que la convercion se ejecute en paralelo
        self.proceso1.start() #inicio el hilo y llamada a funcion start
        
    
    def terminar_proceso(self):
       self.proceso1.terminate()
    
 
    
def inicio():
    app = VideoConverterGUI()    
    return 0


if __name__ == '__main__':
    inicio()








