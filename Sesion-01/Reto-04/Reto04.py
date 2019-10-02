def recomiendamePeliculas(accion, superheroes):
    if(accion == True):
        if(superheroes == True):
            print("Te recomiendo ver Avengers Endgame!")
        else:
            print("Te recomiendo que veas John Wick")
    else:
        if(superheroes == True):
            print("Te recomiendo ver Batman")
        else:
            print("Te recomiendo 500 dias con summer")



print("Resultados:")
recomiendamePeliculas(accion=True,superheroes=True)
recomiendamePeliculas(accion=True,superheroes=False)
recomiendamePeliculas(accion=False,superheroes=True)
recomiendamePeliculas(accion=False,superheroes=False)

