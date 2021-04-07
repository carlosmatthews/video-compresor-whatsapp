from tkinter import*
from tkinter import filedialog
import whatsapp_video_converter

class Aplicacion():
    def __init__(self):
        raiz = Tk()
        raiz.title("video compresor whatsapp")
        raiz.geometry("300x300")
        boton1 = Button
        boton2 = Button
class Button():
    def __init__(self):
        Button(text ="vacio",bg="pale green", command = None, font = ("Arial Bold", 15)).place(x=100,y=25)





my_video = None
def open_file():
    my_video = filedialog.askopenfilename(initialdir = "/",title = "selecione video")
    

    
app = Aplicacion()    

    



Button(text ="selecione video",bg="pale green", command = open_file, font = ("Arial Bold", 15)).place(x=100,y=25)

Button(text = "start", bg = "green", command = start, font = ("Arial Bold", 15)).place(x=100,y=80)


window.mainloop()







