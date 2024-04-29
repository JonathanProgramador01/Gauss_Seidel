from tkinter import Canvas, Entry, PhotoImage, Spinbox

class Interfas:
    def __init__(self):
        self.data = [[]]
        self.text = None
        self.canva = Canvas(width=736, height=670, highlightthickness=0)
        self. Background = PhotoImage(file="fondo.png")
        self.X1 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)
        self.Y1 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)
        self.Z1 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)
        self.R1 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)

        self.X2 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)
        self.Y2 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)
        self.Z2 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)
        self.R2 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)

        self.X3 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)
        self.Y3 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)
        self.Z3 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)
        self.R3 = Entry(width=10, bg="#B0B0B0", highlightthickness=0)
        self.spinbox = Spinbox(from_=0, to=20, width=8, command=self.num_de_iteraciones, bg="#B0B0B0")
        self.spinbox.place(x=340, y=150)

        self.Entradas()

    def num_de_iteraciones(self):
        valor = int(self.spinbox.get())
        return valor
    def Entradas(self):
        self.canva.pack()
        self.Background = PhotoImage(file="fondo.png")
        self.canva.create_image(368, 335, image=self.Background)
        self.canva.create_text(368, 65, font=("Arial Bold", 60), fill="#F6F5F2", text="Gauss Seidel", justify="center")
        self.canva.create_text(115, 650, font=("Arial Bold", 15), fill="#F6F5F2", text="Jonathan Rosas Cedillo",justify="center")

        self.X1.place(x=80, y=220)
        self.canva.create_text(200, 230, font=("Arial Bold", 18), fill="#F6F5F2", text="X + ")

        self.Y1.place(x=250, y=220)
        self.canva.create_text(370, 230, font=("Arial Bold", 18), fill="#F6F5F2", text="Y + ")

        self.Z1.place(x=420, y=220)
        self.canva.create_text(540, 230, font=("Arial Bold", 18), fill="#F6F5F2", text="Z = ")

        self.R1.place(x=590, y=220)


        self.X2.place(x=80, y=290)
        self.canva.create_text(200, 300, font=("Arial Bold", 18), fill="#F6F5F2", text="X + ")

        self.Y2.place(x=250, y=290)
        self.canva.create_text(370, 300, font=("Arial Bold", 18), fill="#F6F5F2", text="Y + ")

        self.Z2.place(x=420, y=290)
        self.canva.create_text(540, 300, font=("Arial Bold", 18), fill="#F6F5F2", text="Z = ")

        self.R2.place(x=590, y=290)


        self.X3.place(x=80, y=360)
        self.canva.create_text(200, 370, font=("Arial Bold", 18), fill="#F6F5F2", text="X + ")

        self.Y3.place(x=250, y=360)
        self.canva.create_text(370, 370, font=("Arial Bold", 18), fill="#F6F5F2", text="Y + ")

        self.Z3.place(x=420, y=360)
        self.canva.create_text(540, 370, font=("Arial Bold", 18), fill="#F6F5F2", text="Z = ")

        self.R3.place(x=590, y=360)

    def obtain_data(self):
        self.data = [[float(self.X1.get()), float(self.Y1.get()), float(self.Z1.get()), float(self.R1.get())],
                 [float(self.X2.get()), float(self.Y2.get()), float(self.Z2.get()), float(self.R2.get())],
                [float(self.X3.get()), float(self.Y3.get()), float(self.Z3.get()), float(self.R3.get())]]

    def limpieza(self):
        self.X1.destroy()
        self.Y1.destroy()
        self.Z1.destroy()
        self.R1.destroy()
        self.X2.destroy()
        self.Y2.destroy()
        self.Z2.destroy()
        self.R2.destroy()
        self.X3.destroy()
        self.Y3.destroy()
        self.Z3.destroy()
        self.R3.destroy()
        self.canva.delete("all")
        self.canva.create_image(368, 340, image=self.Background)
        self.text = self.canva.create_text(380, 350, font=("Arial Bold", 60), fill="#F6F5F2", text="0 %")
        self.spinbox.destroy()




