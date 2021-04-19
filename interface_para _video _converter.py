from tkinter import*
from tkinter import filedialog
#from whatsapp_video_converter import*

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("video compresor whatsapp")
        self.window.geometry("300x200")
        self.boton1 = Button(text ="select video",bg="pale green", command = open_file, font = ("Arial Bold", 12)).place(x=100,y=40)
        self.boton2 = Button(text ="    convert    ", bg = "pale green", command = None, font = ("Arial Bold", 12)).place(x=100,y=80)
        self.buton3 = Button(text ="      stop       ", bg = "pale green", command = None, font = ("Arial Bold", 12)).place(x=100,y=120)
        self.window.mainloop()


mi_video = None
def open_file():
    mi_video = filedialog.askopenfilename(initialdir = "/",title = "selecione video")
    
def inicio():
    app = Aplicacion()    
    return 0

if __name__ == '__main__':
    inicio()




    

"""

Button(text ="selecione video",bg="pale green", command = open_file, font = ("Arial Bold", 15)).place(x=100,y=25)

Button(text = "start", bg = "green", command = start, font = ("Arial Bold", 15)).place(x=100,y=80)
"""








