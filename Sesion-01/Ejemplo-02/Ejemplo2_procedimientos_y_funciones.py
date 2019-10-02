# -*- coding: utf-8 -*-
"""
@author: Dr. Antonio Arista Jalife
"""

def prepararDesayuno():
    print("Buscando ingredientes...")
    print("Eligiendo una receta...")
    print("Cocinando...")
    print("Preparando café...")
    print("Cafe y comida lista! Sirviendo...")
    print("¡El desayuno está listo!")


def abordarElTransporte(nombreDelTransporte,rutaASeguir):
    print("Subiendo a "+nombreDelTransporte)
    print("Yendo por "+rutaASeguir)
    print("¡Has llegado a tu destino!")


def calcularCalorias(tiempoEnHoras):
    tiempoEnMinutos = tiempoEnHoras*60
    calorias = tiempoEnMinutos/3 
    return calorias

def hacerEjercicio(deporte, tiempoEnHoras, equipoAUsar):
    print("Vamos a jugar "+deporte);
    print("Jugarás durante "+str(tiempoEnHoras)+" horas")
    calorias = calcularCalorias(tiempoEnHoras)
    print("Gastaste "+str(calorias)+ " Cals")
    print("con "+equipoAUsar)

prepararDesayuno()
abordarElTransporte("Metrobus","linea 1")
hacerEjercicio("Fútbol",3,"balón")




