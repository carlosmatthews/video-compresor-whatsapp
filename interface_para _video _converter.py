from tkinter import*
from tkinter import filedialog
from back_end_for_gui import*
import threading


class VideoConverter():
 
    def __init__(self):
        self.window = Tk()
        self.window.title("video compresor whatsapp")
        self.window.geometry("300x200")
        self.boton1 = Button(text ="select video",bg="pale green", command = self.open_file, font = ("Arial Bold", 12))
        self.boton1.pack(padx=10, pady=10)
        self.boton2 = Button(text ="    convert    ", bg = "pale green", command = self.llamando_a_start, font = ("Arial Bold", 12))
        self.boton2.pack(padx=10, pady=10)
        self.buton3 = Button(text ="      stop       ", bg = "pale green", command = self.llamando_a_stop, font = ("Arial Bold", 12))
        self.buton3.pack(padx=10, pady=10)
        self.window.mainloop()
                      
    def open_file(self):
        self.mi_video = filedialog.askopenfilename(initialdir = "/",title = "selecione video")

    def llamando_a_start(self):
        hilo1 = threading.Thread(target=start(self.mi_video)) #crea un hilo para que la convercion se ejecute en paralelo
        #self.ejecucion = start(self.mi_video)
        hilo1.start() #inicio el hilo y llamada a funcion start

    def llamando_a_stop(self):
        stop


def inicio():
    app = VideoConverter()    
    return 0


if __name__ == '__main__':
    inicio()




    

"""

Button(text ="selecione video",bg="pale green", command = open_file, font = ("Arial Bold", 15)).place(x=100,y=25)

Button(text = "start", bg = "green", command = start, font = ("Arial Bold", 15)).place(x=100,y=80)
"""








