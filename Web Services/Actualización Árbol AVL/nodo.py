'''
Created on 13/3/2015

@author: Destroy the time
'''
class Nodo:
    #lista doblemente enlazada
    nombreAereopuerto,pais,contrasena="","",""
    izq, der=None, None
    #Arbol AVL vuelos
    lugarLLegada, horafechaLlegada, horafechaSalida, estadoInicial= "","","",""
    cantidadPasajeroPC, cantidadPasajeroCT, cantidadPasajeroCE, idUnico, h = 0,0,0,0,0 
        
    def __initAereo__(self, nombreAereopuerto, pais, contrasena):
            self.nombreAereopuerto=nombreAereopuerto
            self.pais=pais
            self.contrasena=contrasena
            self.izq=None
            self.der=None
            
    def __initVuelos__(self, lugarLlegada, horafechaLlegada, horafechaSalida, cantidadPasajeroPC, cantidadPasajeroCT, cantidadPasajeroCE,
                       estadoInicial, idUnico,h):
        self.lugarLlegada=lugarLlegada
        self.horafechaLlegada=horafechaLlegada
        self.horafechaSalida=horafechaSalida
        self.cantidadPasajeroPC=cantidadPasajeroPC
        self.cantidadPasajeroCT=cantidadPasajeroCT
        self.cantidadPasajeroCE=cantidadPasajeroCE
        self.estadoInicial=estadoInicial
        self.idUnico=idUnico
        self.h=h
        self.izq=None
        self.der=None
  
        
    def setIzq(self, izq):
        self.izq=izq
    def getIzq(self):
        return self.izq
    def setDer(self, der):
        self.der=der
    def getDer(self):
        return self.der
    def setNombreAereopuerto(self, nombreAereopuerto):
        self.nombreAereopuerto=nombreAereopuerto
    def getNombreAereopuerto(self):
        return self.nombreAereopuerto
    def setPais(self, pais):
        self.pais=pais
    def getPais(self):
        return self.pais
    def setContrasena(self, contrasena):
        self.contrasena=contrasena
    def getContrasena(self):
        return self.contrasena