# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Destroy the time"
__date__ = "$13-mar-2015 13:20:39$"



class AVLVuelos:
    def __ini__(self):
        self.raiz=None
    
    def insertarAVLVUELOS(self,lugarLlegada, horaLlegada, fechaLlegada, horaSalida, fechaSalida, cantidadPasajeroPC, cantidadPasajeroCT,
    cantidadPasajeroCE, costoPC, costoCT, costoCE, estadoInicial, idUnico, h):
        if self.raiz==None:
            self.raiz=Nodo(lugarLlegada, horaLlegada, fechaLlegada, horaSalida, fechaSalida,cantidadPasajeroPC, cantidadPasajeroCT,
            cantidadPasajeroCE, costoPC, costoCT, costoCE, estadoInicial, idUnico, h)
            h=1
        else:
           if idUnico < self.raiz.idUnico:
               self.raiz.izq=insertarAVLVUELOS(self.raiz.der, lugarLlegada, horaLlegada, fechaLlegada, horaSalida, fechaSalida, cantidadPasajeroPC, cantidadPasajeroCT,
               cantidadPasajeroCE, costoPC, costoCT, costoCE, estadoInicial, idUnico,h)
               
               if (altura(self.raiz.izq)- altura(self.raiz.der)) ==2:
                 if idUnico < self.raiz.izq.idUnico:
                    #Rotar II
                 else:
                     #print "rotar ID"#Rotar ID        
            else if idUnico > self.raiz.idUnico:
                self.raiz.der=insertarAVLVUELOS(self.raiz.der, lugarLlegada,horaLlegada, fechaLlegada, horaSalida, fechaSalida,
                cantidadPasajeroPC, cantidadPasajeroCT, cantidadPasajeroCE, costoPC, costoCT, costoCE, estadoInicial, idUnico, h)
                
                      if (altura(self.raiz.der)- altura(self.raiz.izq)) ==2:
                        if idUnico > self.raiz.der.idUnico:
                        #rotar DD
                        else:
                        #rotar DI
    self.raiz.h=max((altura(raiz.iz), altura(raiz.der))+1)
    return self.raiz

    def altura(self)
    if self.raiz== None:
        return -1
    else:
        return raiz.h
    
    def rotarII(self):
        n1=self.n.izq;
        
        n.izq=n1.der
        n1.der=n
        
        n.h=max((altura(n.izq), altura(n.der))+1)
        n1.h=max((altura(n.izq), n.h)+1)
        
        return n1
    
    def rotarDD(self):
        n1=self.n.der
        self.n.der=n1.izq
        n1.izq=self.n
        
        self.n.h=max((altura(self.n.izq), altura(self.n.der))+1)
        n1.h=max((altura(n1.der), self.ne.h)+1)
        return n1
    
    def rotarID(self):
        self.n.iz=rotarDD(self.n.izq)
        return rotarII(self.n)
    
    def rotarDI(self):
        self.n.der=rotarII(self.n.der)
        return rotarDD(self.n)
        
