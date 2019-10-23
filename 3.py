def bin(x,y):
    if int(x)==0 or int(x)==1:
        x=bool(x)
    else:
        return 'Entrada inválida!'
    if int(y)==0 or int(y)==1:
        y=bool(y)
    else:
        return 'Entrada inválida!'
    
    if not x and not y:
        return False
    if y and not x:
        return True
    if x and not y:
        return False
    if x and y:
        return True
