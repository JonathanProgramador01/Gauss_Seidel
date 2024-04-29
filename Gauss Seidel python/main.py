from tkinter import *
from Gui import Interfas
from Word import Word
from Cerebro import Brain


Window = Tk()
Window.title("Gauss Seidel")
Ventana = Interfas()


def contador(flag, count=1):

    if count <= 100:
        Ventana.canva.itemconfig(Ventana.text, text=f"{count}%")
        Window.after(10,contador,flag,count+1)
    else:
        if flag == 1:
            Ventana.canva.itemconfig(Ventana.text, text="Error Ingresa bien los datos", font=("Arial Bold", 30))
        else:
            Ventana.canva.itemconfig(Ventana.text, text="Metodo Creado Exitosamente", font=("Arial Bold", 30))
def Accion():

    try:
        Ventana.obtain_data()
    except ValueError:
        contador(flag=1)
    else:
        contador(flag=0)
        Documento = Word(Ventana.data)
        cerebro = Brain(Documento.return_lista())
        Documento.checar_si_esta_acomodada_tu_ecuacion(cerebro.acomodar())
        Documento.despeje()
        Documento.tabla(cerebro.obtener_iteraciones(Ventana.num_de_iteraciones()),Ventana.num_de_iteraciones())
        Documento.cerrar_documento()



    finally:
        Ventana.limpieza()
        button.destroy()













button = Button(text="Calcular", font=("Arial Bold", 28), command=Accion)
button .config(width=10)
button .place(x=260, y=480)


Window.mainloop()
























