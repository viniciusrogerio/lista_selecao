def informaEstacao(mes,hemisf):
    mes=int(mes)
    hemisf=hemisf.upper()
    if hemisf=='NORTE':
        if mes==12 or mes==1 or mes==2:
            estacao='Inverno'
        elif mes==3 or mes==4 or mes==5:
            estacao='Primavera'
        elif mes==6 or mes==7 or mes==8:
            estacao='Verão'
        elif mes==9 or mes==10 or mes==11:
            estacao='Outono'
        else:
            estacao=False
    elif hemisf=='SUL':
        if mes==12 or mes==1 or mes==2:
            estacao='Verão'
        elif mes==3 or mes==4 or mes==5:
            estacao='Outono'
        elif mes==6 or mes==7 or mes==8:
            estacao='Inverno'
        elif mes==9 or mes==10 or mes==11:
            estacao='Primavera'
        else:
            estacao=False
    else:
        estacao=False
    if (estacao):
        return estacao
    else:
        return "Mês ou hemisfério inválido!"
