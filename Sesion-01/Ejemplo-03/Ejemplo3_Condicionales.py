# -*- coding: utf-8 -*-
"""
@author: Dr. Antonio Arista Jalife
"""
def salirDePaseo(estaLloviendo, traesParaguas):
    print("Saldremos de paseo?...")
    if(estaLloviendo == True):
        if(traesParaguas == True):
            print("Ok! vamos a salir!")
        else:
            print("No creo que sea una buena idea")
    else:
        print("Ok! vamos a salir!")
        
salirDePaseo(True, True)
