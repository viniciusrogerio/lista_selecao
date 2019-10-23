def operacaoLogica(x,y,op):
    if int(x)==0 or int(x)==1:
        x=bool(x)
    else:
        return 'Entrada inválida!'
    if int(y)==0 or int(y)==1:
        y=bool(y)
    else:
        return 'Entrada inválida!'
    
    op=op.upper()
    
    if op == 'OR':
        if x or y:
            return True
        else:
            return False
    elif op == 'AND':
        if x and y:
            return True
        else:
            return False
    elif op == 'NOR':
        if not x and not y:
            return True
        else:
            return False
    elif op == 'NAND':
        if x and y:
            return False
        else:
            return True
    elif op == 'XOR':
        if (x and not y) or (y and not x):
            return True
        else:
            return False
    else:
        return 'Operação inválida!'
