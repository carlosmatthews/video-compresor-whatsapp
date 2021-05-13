from tkinter import*
from tkinter import filedialog
from backend import*
import threading


class VideoConverterGUI():
 
    def __init__(self):
        self.mi_video = None
        self.window = Tk()
        self.window.title("video compresor whatsapp")
        self.window.geometry("300x200")
        self.boton1 = Button(text ="select video",bg="pale green", command = self.open_file, font = ("Arial Bold", 12))
        self.boton1.pack(padx=10, pady=10)
        self.boton2 = Button(text ="    convert    ", bg = "pale green", command = self.crear_hilo, font = ("Arial Bold", 12))
        self.boton2.pack(padx=10, pady=10)
        self.boton3 = Button(text ="      stop       ", bg = "pale green", command = self.terminar_hilo, font = ("Arial Bold", 12))
        self.boton3.pack(padx=10, pady=10)
        self.window.mainloop()
                      
    def open_file(self):
        self.mi_video = filedialog.askopenfilename(initialdir = "/",title = "selecione video")
    
    
    
    def crear_hilo(self):
        llamando_a_start = lambda: start(self.mi_video)    
        self.hilo1 = threading.Thread(target=llamando_a_start)
        self.hilo1.start()
    def terminar_hilo(self):
        self.hilo1._stop() # este es una metodo no documentado que podria deprecarce
 
 

def inicio():
    app = VideoConverterGUI()    
    return app



if __name__ == '__main__':
    app = inicio()








