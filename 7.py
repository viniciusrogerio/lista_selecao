def triangulo(x,y,z):
    x=float(x)
    y=float(y)
    z=float(z)
    if x+y > z and y+z > x and x+z > y:
        if x == y:
            if y == z:
                print('É equilátero!')
            else:
                print('É isósceles!')
        elif x == z:
            if z == y:
                print('É equilátero!')
            else:
                print('É isósceles!')
        elif y == z:
            if z == x:
                print('É equilátero!')
            else:
                print('É isósceles!')
        else:
            print('É escaleno!')
    else:
        print('Os lados informados não formam um triângulo!')
