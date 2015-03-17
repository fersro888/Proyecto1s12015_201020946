'''
Created on 13/3/2015

@author: Destroy the time
'''
import os.path
import nodo
import subprocess
from sys import stderr


class ListaDoblementeEnlazada(): 
   
    archivoDOT=""
    def __init__(self):
        self.raiz=None
       
        
    def crearnodo(self,nombreAereopuerto, pais, contrasena):
        
        if self.raiz==None:
            n= nodo.Nodo()
            n.__initAereo__(nombreAereopuerto, pais, contrasena) #primero crear una instancia de este objeto para utilizar los constructores
            self.raiz=n
            print "estoy creando el primer nodo "
        else:
            n= nodo.Nodo()
            n.__initAereo__(nombreAereopuerto, pais, contrasena)
            n.setDer(self.raiz)
            self.raiz.setIzq(n)
            #n=self.raiz
            self.raiz=n
            print "Estoy en la segunda condicion " 
        return self.raiz
    
    def recorrerlde(self, cabeza):
        if cabeza != None :
            if cabeza.getDer()==None:
                enviarDOT=cabeza.getNombreAereopuerto()+"\n"
                self.archivoDOTAEREOPUERTO(enviarDOT)
                cabeza==None
            else:
                enviarDOT=cabeza.getNombreAereopuerto()+" -> "+ cabeza.getDer().getNombreAereopuerto()+"\n"
                self.archivoDOTAEREOPUERTO(enviarDOT)
           # print "Lista doblemente enlazada", aux1.nombreAereopuerto, "->", aux2.nombreAereopuerto
            self.recorrerlde(cabeza.getDer())
        else:
            print "no puedo recorrer ", self.raiz.nombreAereopuerto
            
            
    def DOT(self, cabeza):
        
            archivoDOT="Digraph {\n rankdir=LR;\n"
            archivoDOT= archivoDOT+ self.raiz.getNombreAereopuerto()+" [label="+self.raiz.getNombreAereopuerto()+",shape=box];\n"
            #self.archivoDOTAEREOPUERTO(archivoDOT)
            
            aux=cabeza
            aux1=cabeza.getDer()
            while aux1!=None :
                
                archivoDOT= archivoDOT+aux.getNombreAereopuerto()+" [label="+aux.getNombreAereopuerto()+",shape=box];\n"
                archivoDOT= archivoDOT+aux1.getNombreAereopuerto()+" [label="+aux1.getNombreAereopuerto()+",shape=box];\n"
                archivoDOT= archivoDOT+ aux.getNombreAereopuerto()+ " -> "+ aux1.getNombreAereopuerto()+";\n"
                archivoDOT= archivoDOT+ aux1.getNombreAereopuerto()+ " -> "+ aux.getNombreAereopuerto()+ ";\n"
                aux=aux1;
                aux1=aux1.getDer()
                
            archivoDOT=archivoDOT+"}"        
            self.archivoDOTAEREOPUERTO(archivoDOT)
            
    def archivoDOTAEREOPUERTO(self, DOT):    
        nombreArchivo= open("C://DotPython//Aereopuertos.dot","w")
        d=str(DOT)
        file.write(nombreArchivo,d)
        file.close(nombreArchivo)
        
        #Comando= raw_input("C://DDot//dot.exe -Tpng C://DotPython//Aereopuertos.dot -o Aereopuertos.png")

       # Proceso= subprocess.Popen(
        # [Comando],
        # stdout= subprocess.PIPE,
         #stderr= subprocess.PIPE,
         #shell=True     )           
        #out, error = Proceso.communicate()         
        #print out 
        #print Cmd("C://DDot//dot.exe -Tpng C://DotPython//Aereopuertos.dot -o Aereopuertos.png")
        #os.system("C:/DDot/dot.exe -Tpng cd C:/DotPython/Aereopuertos.dot -o Aereopuertos.png")
        