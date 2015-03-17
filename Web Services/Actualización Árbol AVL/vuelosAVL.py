'''
Created on 13/3/2015

@author: Destroy the time
'''
import nodo

class AVLVuelos:
    def __init__(self):
        self.raizVuelo=None
        self.contador=0
        self.archivoDOT="Digraph g{\n node [shape=record, height=.1];\n"
        self.datoDOT=""
        self.archivodDOTCIERRE="}"
    def insertarAVLVUELOS(self,cabeza,lugarLlegada, horafechaLlegada, horafechaSalida, cantidadPasajeroPC, cantidadPasajeroCT,
    cantidadPasajeroCE, estadoInicial, idUnico, h):
    
        if cabeza==None:
            cabeza=nodo.Nodo()
            cabeza.__initVuelos__(lugarLlegada, horafechaLlegada, horafechaSalida,cantidadPasajeroPC, cantidadPasajeroCT,
            cantidadPasajeroCE, estadoInicial, idUnico, h)
        else:
            if idUnico < cabeza.idUnico:
                    print "estoy en el nodo izquierdo------------"+ cabeza.idUnico
                    cabeza.izq=self.insertarAVLVUELOS(cabeza.izq,lugarLlegada, horafechaLlegada, horafechaSalida, cantidadPasajeroPC, cantidadPasajeroCT,
                    cantidadPasajeroCE, estadoInicial, idUnico,h)  
                     
                    if (self.altura(cabeza.izq)- self.altura(cabeza.der)) ==2:
                        if idUnico > cabeza.izq.idUnico:
                            print "estoy rotando II, factor de equilibrio"+ str(cabeza.h)
                            cabeza=self.rotarII(cabeza)#rotar DD
                            
                        else:
                            print "estoy rotando ID, factor de equilibrio"+ str(cabeza.h)
                            cabeza=self.rotarID(cabeza)#rotar DI 
 
                    else:
                        if(cabeza.izq==None):
                            cabeza.h=-1
                        if(cabeza.der==None):
                            cabeza.h=1
                        if(cabeza.izq!=None and cabeza.der!=None):
                            cabeza.h=0
   
            if idUnico > cabeza.idUnico:
                    print "estoy en el nodo derecho---------"+ cabeza.idUnico
                    cabeza.der=self.insertarAVLVUELOS(cabeza.der,lugarLlegada,horafechaLlegada, horafechaSalida,
                    cantidadPasajeroPC, cantidadPasajeroCT, cantidadPasajeroCE, estadoInicial, idUnico, h)
                    if (self.altura(cabeza.der)- self.altura(cabeza.izq)) ==2:
                        if idUnico > cabeza.der.idUnico:
                            print "estoy rotando DD, factor de equilibrio"+ str(cabeza.h)
                            cabeza=self.rotarDD(cabeza)#rotar DD
                        
                        else:
                            print "estoy rotando DI, factor de equilibrio"+ str(cabeza.h)
                            cabeza=self.rotarDI(cabeza)#rotar DI 
         
                    else:
                        if(cabeza.izq==None):
                            cabeza.h=1
                        if(cabeza.der==None):
                            cabeza.h=-1
                        if(cabeza.izq!=None and cabeza.der!=None):
                            cabeza.h=0

        return cabeza
                            

    def DOT(self, cabeza):
        #archivoDOT="Digraph {\n"   
  
        if cabeza!=None: 
            self.recorridoPREORDEN(cabeza)
            self.DOT(cabeza.izq)
            self.DOT(cabeza.der)     
        #archivoDOT=archivoDOT+"}"
       # self.archivoDOTAEREOPUERTO(archivoDOT)
        
    def recorridoPREORDEN(self, raiz):
        
        self.datoDOT=self.datoDOT+"node"+raiz.idUnico+"[label=\"<f0> | <f1>"+raiz.idUnico+"--"+raiz.estadoInicial+"|<f2>\"];\n"
        
        if(raiz.izq!=None):
            print "mi izquierdo es"+raiz.izq.idUnico
            self.datoDOT=self.datoDOT+"node"+raiz.izq.idUnico+"[label=\"<f0> | <f1>"+raiz.izq.idUnico+" -- "+raiz.izq.estadoInicial+"-- "+str(raiz.izq.h)+"|<f2>\"];\n"
            self.datoDOT=self.datoDOT+"node"+raiz.idUnico+"[label=\"<f0> | <f1>"+raiz.idUnico+" -- "+raiz.estadoInicial+" -- "+str(raiz.h)+"|<f2>\"];\n"
            self.datoDOT=self.datoDOT+"node"+raiz.idUnico+":f0 -> "+"node"+raiz.izq.idUnico+":f1;\n"
            
        if(raiz.der!=None):
            print "mi derecho es"+ raiz.der.idUnico
            self.datoDOT=self.datoDOT+"node"+raiz.der.idUnico+"[label=\"<f0> | <f1>"+raiz.der.idUnico+" -- "+raiz.der.estadoInicial+" -- "+str(raiz.der.h)+"|<f2>\"];\n"
            self.datoDOT=self.datoDOT+"node"+raiz.idUnico+"[label=\"<f0> | <f1>"+raiz.idUnico+" -- "+raiz.estadoInicial+" -- "+str(raiz.h)+"|<f2>\"];\n"
            self.datoDOT=self.datoDOT+"node"+raiz.idUnico+":f2 -> "+"node"+raiz.der.idUnico+":f1;\n"


    def archivoDOTAEREOPUERTO(self, DOT):    
        nombreArchivo= open("C://DotPython//VuelosAVL.dot","w")
        d=str(DOT)
        file.write(nombreArchivo,d)
        file.close(nombreArchivo)
   
    def altura(self, raiz):
        if raiz== None:
            return -1
        else:
            #print "estoy en "+str(raiz.h)+" de "+raiz.idUnico
            return raiz.h
    
    def rotarII(self, n):
        n1=n.izq;
        n.izq=n1.der
        n1.der=n
        n.h=max((self.altura(n.izq)+1, self.altura(n.der)+1)) #Recalculando factor de equilibrio
        n1.h=max((self.altura(n.izq)+1, n.h+1))        
        return n1
    
    def rotarDD(self,n):
        n1=n.der
        n.der=n1.izq
        n1.izq=n
        n.h=max(self.altura(n.izq)+1, self.altura(n.der)+1) #Recaulculando factor de equilibrio
        n1.h=max((self.altura(n1.der)+1, n.h+1))
        return n1
    
    def rotarID(self,n):
        n=self.rotarDD(n)
        return self.rotarII(n)
    
    def rotarDI(self,n):
        n=self.rotarII(n)
        return self.rotarDD(n)
