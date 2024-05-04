from tkinter import *
from Gui import Interfas
from Word import Word
from Cerebro import Brain


Window = Tk()
Window.title("Metodo de (Gauss-Seidel o jacobi)")
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
def Accion_de_jakobi():

    try:
        Ventana.obtain_data()
    except ValueError:
        contador(flag=1)
    else:
        contador(flag=0)
        Documento = Word(Ventana.data,"Jacobi")
        cerebro = Brain(Documento.return_lista())
        Documento.checar_si_esta_acomodada_tu_ecuacion(cerebro.acomodar())
        Documento.despeje()
        Documento.tabla(cerebro.obtener_iteraciones_de_jacobi(Ventana.num_de_iteraciones()), Ventana.num_de_iteraciones())
        Documento.cerrar_documento("Jacobi")



    finally:
        Ventana.limpieza()
        gauss.destroy()
        jacobi.destroy()




def Accion_de_Guass():

    try:
        Ventana.obtain_data()
    except ValueError:
        contador(flag=1)
    else:
        contador(flag=0)
        Documento = Word(Ventana.data, "Gauss-Seidel")
        cerebro = Brain(Documento.return_lista())
        Documento.checar_si_esta_acomodada_tu_ecuacion(cerebro.acomodar())
        Documento.despeje()
        Documento.tabla(cerebro.obtener_iteraciones_de_guass_seidel(Ventana.num_de_iteraciones()), Ventana.num_de_iteraciones())
        Documento.cerrar_documento("Gauss-Seidel")


    finally:
        Ventana.limpieza()
        gauss.destroy()
        jacobi.destroy()












gauss = Button(text="Gauss-Seidel", font=("Arial Bold", 28), command=Accion_de_Guass, width=10,highlightthickness=0, bg="#76777B")
jacobi = Button(text="Jacobi", font=("Arial Bold", 28), command=Accion_de_jakobi, width=10, highlightthickness=0, bg="#76777B")


gauss .place(x=78, y=380)
jacobi .place(x=435, y=380)


Window.mainloop()
























