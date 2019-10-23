def exibeCrescente(x,y,z):
    if x!=y and y!=z and x!=z: #se forem três distintos
        if x < y:
            if y < z:
                print(x,y,z)
            else:
                if x < z:
                    print(x,z,y)
                else:
                    print(z,x,y)
        else:
            if y < z:
                if x < z:
                    print(y,x,z)
                else:
                    print(y,z,x)
            else:
                print(z,y,x)
    else:
        print('Entrada inválida! Informe três números distintos.')
        
