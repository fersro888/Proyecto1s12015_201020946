# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Destroy the time"
__date__ = "$11-mar-2015 20:19:25$"

import nodo


class ListaDoblementeEnlazada:
    def __init__(self):
        self.raiz=None
        
    def crearnodo(self, nombreAereopuerto, pais, contrasena):
        if self.raiz==None:
            nuevo= Nodo(nombreAereopuerto, pais, contrasena)
            self.raiz=nuevo
        else:
            nuevo=Nodo(nombreAereopuerto, pais, contrasena)
            nuevo.der=self.raiz
            self.raiz.izq=nuevo
            self.raiz=nuevo
            
        return self.raiz

    def recorrerlde(self, raiz):
        if self.raiz != None and self.raiz.der != None:
            aux1= self.raiz
            aux2= self.raiz.der
            print "Lista doblemente enlazda", aux1.nombreAereopuerto, "->", aux2.nombreAereopuerto
            recorrerlde(raiz.der)
        
