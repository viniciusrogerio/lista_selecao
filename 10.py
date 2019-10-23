def multiplos(n,i,j):
    if n > 0 and i != 0 and j != 0:
        for x in range(n+1):
            if x%i == 0 or x%j == 0:
                if x%2 == 0:
                    print(x,end=' ')
    else:
        print('Entrada inválida!')
