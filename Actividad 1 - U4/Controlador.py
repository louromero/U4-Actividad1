from Vista import Vista

class Controlador:
    __vista=None

    def __init__(self):
        self.__vista=Vista()
        self.calcular()
        self.botonlimpiar()
        self.__vista.iniciar()

    def calcular(self):
        funcion   = self.setInfo
        boton     = self.__vista.getBotonC()
        boton.config(command = funcion)

    def botonlimpiar(self):
        arreglo = self.__vista.getLimpiar()
        arreglo.pop(0).config(command=lambda : [self.limpiar(e) for e in arreglo] )

    def limpiar(self,entrada):
            entrada.set("")

    def setInfo(self):
        info1 = ""
        info2 = ""
        try:
            kilos  = float(self.__vista.getPeso())
            altura = float(self.__vista.getAltura())
            imc    = kilos / ((altura/100)*(altura/100))
        except :
            pass
        else:
            if   imc < 18.5:
                info2 = "Peso inferior al normal"
            elif imc > 18.5 and imc < 24.9:
                info2 = "PESO NORMAL"
            elif imc > 25 and imc < 29.9:
                info2 = "Peso superior al normal"
            else:
                info2 = "Obesidad"

            imc    = str("{:,.2f}".format(imc))
            info1   = "Tu indice de masa corporal (IMC) es: {} kg/m2".format(imc)
        self.__vista.setInfo(info1,info2)
