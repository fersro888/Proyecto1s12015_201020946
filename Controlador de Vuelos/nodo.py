# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Destroy the time"
__date__ = "$13-mar-2015 13:08:03$"

class Nodo:
    #lista doblemente enlazada
    izq, der=None,None
    nombreAereopuerto,pais,contrasena="","",""
    #Arbol AVL vuelos
    lugarLLegada, horaLlegada, fechaLlegada, horaSalida, fechaSalida, estadoInicial= "","","","","",""
    cantidadPasajeroPC, cantidadPasajeroCT, cantidadPasajeroCE, idUnico, h = 0,0,0,0,0
    costoPC, costoCT, costoCE=0.0,0.0,0.0
    def __init__(self, nombreAereopuerto, pais, contrasena):
            self.nombreAereopuerto=nombreAereopuerto
            self.pais=pais
            self.contrasena=contrasena
            self.izq=None
            self.der=None
            
    def __init__(self, lugarLlegada, horaLlegada, fechaLlegada, horaSalida, fechaSalida, cantidadPasajeroPC, cantidadPasajeroCT, cantidadPasajeroCE,costoPC, costoCT, costoCE):
        self.lugarLlegada=lugarLlegada
        self.horaLlegada=horaLlegada
        self.fechaLlegada= fechaLlegada
        self.horaSalida=horaSalida
        self.fechaSalida=fechaSalida
        self.cantidadPasajeroPC=cantidadPasajeroPC
        self.cantidadPasajeroCT=cantidadPasajeroCT
        self.cantidadPasajeroCE=cantidadPasajeroCE
        self.costoPC=costoPC
        self.costoCT=costoCT
        self.costoCE=costoCE


