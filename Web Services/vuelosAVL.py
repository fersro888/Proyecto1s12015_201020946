'''
Created on 13/3/2015

@author: Destroy the time
'''
import nodo

class AVLVuelos:
    def __init__(self):
        self.raizVuelo=None
    
    def insertarAVLVUELOS(self,lugarLlegada, horafechaLlegada, horafechaSalida, cantidadPasajeroPC, cantidadPasajeroCT,
    cantidadPasajeroCE, estadoInicial, idUnico, h):
        self.insertarAVLVUELO(self.raizVuelo, lugarLlegada, horafechaLlegada, horafechaSalida, cantidadPasajeroPC, 
         cantidadPasajeroCT, cantidadPasajeroCE, estadoInicial, idUnico, h)
    
    def insertarAVLVUELO(self,raizVuelo,lugarLlegada, horafechaLlegada, horafechaSalida, cantidadPasajeroPC, cantidadPasajeroCT,
    cantidadPasajeroCE, estadoInicial, idUnico, h):
    
        if self.raizVuelo==None:
            nuevo=nodo.Nodo()
            nuevo.__initVuelos__(lugarLlegada, horafechaLlegada, horafechaSalida,cantidadPasajeroPC, cantidadPasajeroCT,
            cantidadPasajeroCE, estadoInicial, idUnico, h)
            self.raizVuelo=nuevo
            print "primer nodo-> cabeza"
        else:
            if idUnico < self.raizVuelo.idUnico:
                print "estoy en el nodo izquierdo"
                self.raizVuelo.izq=self.insertarAVLVUELO(self.raizVuelo.izq, lugarLlegada, horafechaLlegada, horafechaSalida, cantidadPasajeroPC, cantidadPasajeroCT,
                cantidadPasajeroCE, estadoInicial, idUnico,h)
               
            if (self.altura(self.raizVuelo.izq)- self.altura(self.raizVuelo.der)) == 2:
                    if idUnico < self.raizVuelo.izq.idUnico:
                        self.rotarII(self.raizVuelo)#Rotar II
                    else:
                        self.rotarID(self.raizVuelo)#Rotar ID  
                    
            elif idUnico > self.raizVuelo.idUnico:
                        print "estoy en el nodo derecho"
                        self.raizVuelo.der=self.insertarAVLVUELO(self.raizVuelo.der, lugarLlegada,horafechaLlegada, horafechaSalida,
                        cantidadPasajeroPC, cantidadPasajeroCT, cantidadPasajeroCE, estadoInicial, idUnico, h)
                
            if (self.altura(self.raizVuelo.der)- self.altura(self.raizVuelo.izq)) ==2:
                        if idUnico > self.raizVuelo.der.idUnico:
                            self.rotarDD(self.raizVuelo)#rotar DD
                        else:
                            self.rotarDI(self.raizVuelo)#rotar DI
        self.raizVuelo.h=max((self.altura(self.raizVuelo.izq)+1, self.altura(self.raizVuelo.der)+1))
        return self.raizVuelo


    def altura(self, raiz):
        if self.raizVuelo== None:
            return -1
        else:
            return self.raizVuelo.h
    
    def rotarII(self):
        n1=self.n.izq;
        
        self.n.izq=n1.der
        n1.der=self.n
        
        self.n.h=max((self.altura(self.n.izq), self.altura(self.n.der))+1)
        n1.h=max((self.altura(self.n.izq), self.n.h)+1)
        
        return n1
    
    def rotarDD(self):
        n1=self.n.der
        self.n.der=n1.izq
        n1.izq=self.n
        
        self.n.h=max((self.altura(self.n.izq), self.altura(self.n.der))+1)
        n1.h=max((self.altura(n1.der), self.ne.h)+1)
        return n1
    
    def rotarID(self):
        self.n.iz=self.rotarDD(self.n.izq)
        return self.rotarII(self.n)
    
    def rotarDI(self):
        self.n.der=self.rotarII(self.n.der)
        return self.rotarDD(self.n)
