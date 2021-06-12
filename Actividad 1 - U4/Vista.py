from tkinter import *
from tkinter import ttk

class Vista:

    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry('500x300')
        self.__ventana.title("Calculadora de IMC")

        mainFrame = ttk.Frame(self.__ventana,padding=(70,50))
        mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        titulo = ttk.Label(mainFrame, text="Calculadora de IMC",anchor="c")
        self.form = ttk.Frame(mainFrame, padding=(10, 10))
        self.__frameSec = ttk.Frame(mainFrame, padding=(10, 12))

        #Se declaran las variables
        self.__altura = DoubleVar()
        self.__kilos  = DoubleVar()
        self.__info1  = StringVar()
        self.__info2  = StringVar()

        #ALTURA
        self.etiqueta1 = ttk.Label(self.form,text="Altura: ",padding=(5,5))
        self.labelAux1 = ttk.Label(self.form,text="cm",padding=(1,1))
        self.entrada1  = ttk.Entry(self.form,width=45,textvariable=self.__altura)

        #PESO
        self.etiqueta2 = ttk.Label(self.form , text="Peso: ",padding=(5,5))
        self.labelAux2 = ttk.Label(self.form, text="kg", padding=(1, 1))
        self.entrada2  = ttk.Entry(self.form, width=45 , textvariable=self.__kilos)
        self.boton1    = ttk.Button(mainFrame ,text="Calcular",padding=(30,8))
        self.boton2    = ttk.Button(mainFrame , text="Limpiar",padding=(30,8))

        self.__Linfo1    = ttk.Label(self.__frameSec,textvariable=self.__info1)
        self.__Linfo2    = ttk.Label(self.__frameSec,textvariable=self.__info2)


        style = ttk.Style()
        style.configure("TLabelframe", borderwidth=0, highlightthickness=0)
        style.configure("titulo.TLabel", font=("arial",20))

        #BOORDE DEL BOTON
        style.configure("TButton", background="#60CC64")
        style.configure("TLabel", background="#fff", font='arial')
        

        #FONDO
        style.configure("TFrame",background="#fff")
        style.configure("BW.Label", font=("Roboto"), background="#fff")

        titulo.configure(style="titulo.TLabel")
        self.etiqueta1.configure(style="BW.Label")
        self.etiqueta2.configure(style="BW.Label")

        #Se establecen las posiciones de los componentes visuales
        titulo.grid(row=0,column=0,columnspan=2)
        self.form.grid(column=0, row=1,columnspan=2)
        self.etiqueta1.grid(row=1,column=1)
        self.entrada1.grid(row=1,column=2)
        self.labelAux1.grid(row=1,column=3)

        self.etiqueta2.grid(row=2,column=1)
        self.entrada2.grid(row=2, column=2)
        self.labelAux2.grid(row=2, column=3)

        self.boton1.grid(row=4, column=0)
        self.boton2.grid(row=4, column=1)
        self.__frameSec.grid(row=3,column=0,columnspan=2)
        self.__Linfo1.grid(row=0, column=0,columnspan=2)
        self.__Linfo2.grid(row=1, column=0, columnspan=2)


    def getLimpiar(self):
        return [self.boton2,self.__altura,self.__kilos,self.__info1, self.__info2]

    #Fija la informacion en el label correspondiente
    def setInfo(self,info1,info2):
        if info2 == "" :
            self.__info1.set("Valor incorrecto")
            self.__info2.set("")
        else:
            self.__info1.set(info1)
            self.__info2.set(info2)

    #Getters
    def getBotonC(self):
        return self.boton1

    def getAltura(self):
        return self.__altura.get()

    def getPeso(self)  :
        return self.__kilos.get()

    #Inicia la aplicacion
    def iniciar(self):
        self.__ventana.mainloop()