'''
Created on 8/3/2015

@author: Destroy the time
'''
from flask import Flask, jsonify,request
import json
import LDE
import nodo
import vuelosAVL
from json import dump
from cookielib import debug

app=Flask(__name__)

@app.route('/ListaDE', methods=['POST'])
def lista():

    json=request.json
    #creando un diccionario para obtener cada valor
    diccionario=json
    nombreAereopuerto=diccionario['nombre']
    pais=diccionario['pais']
    contrasena=diccionario['contrasena']
    #estos valores se van a mi objeto Nodo     
    cabeza=nuevo.crearnodo(nombreAereopuerto, pais, contrasena) #Crear mi lista enlazada
    nuevo.DOT(cabeza)
    print (json)
    return jsonify(json) #me devuelve un objeto JSON

@app.route('/arbolAVLVUELO', methods=['POST'])
def arbolVueloAVL():
    json= request.json
    diccionario=json
    
    fechaLlegada=diccionario['fechaLlegada']
    fechaHoraSalida=diccionario['fechaHoraSalida']
    fechaHoraLlegada= diccionario['fechaHoraLlegada']
    primeraClase=diccionario['primeraClase']
    claseTurista=diccionario['claseTurista']
    claseEjecutivo= diccionario['claseEjecutivo']
    estadoInicial= diccionario['estadoInicial']
    idUnico= diccionario['idUnico']
    
    aereopuerto.insertarAVLVUELOS(fechaLlegada, fechaHoraSalida, fechaHoraLlegada, primeraClase, claseTurista, claseEjecutivo, estadoInicial, idUnico,0)
    
    print(json)
    return jsonify(json)
if __name__ == '__main__':
    
    nuevo= LDE.ListaDoblementeEnlazada()
    aereopuerto= vuelosAVL.AVLVuelos()
    app.run(debug=True)
    
    
         
   