def maior_menor(x,y,z):
    lista_resultado=[]
    if x >= y and x >= z:
        if y >= z:
            lista_resultado=[z,x]
        else:
            lista_resultado=[y,x]
    if y >= x and y >= z:
        if x >= z:
            lista_resultado=[z,y]
        else:
            lista_resultado=[x,y]
    if z >= x and z >= y:
        if x >= y:
            lista_resultado=[y,z]
        else:
            lista_resultado=[x,z]
    return lista_resultado
