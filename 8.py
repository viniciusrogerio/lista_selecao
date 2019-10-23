from random import randint
def jokenpo(op):
    op=int(op)
    if op == 1 or op == 2 or op == 3:
        #faz tudo
        comp=randint(1,4)
        if op == comp:
            print('Empate!')
        else:
            if op == 1:
                print('Usuário escolheu pedra.')
                if comp == 2:
                    print('Computador escolheu papel.')
                    user_wins=False
                else:
                    print('Computador escolheu tesoura.')
                    user_wins=True
            elif op == 2:
                print('Usuário escolheu papel.')
                if comp == 1:
                    print('Computador escolheu pedra.')
                    user_wins=True
                else:
                    print('Computador escolheu tesoura.')
                    user_wins=False
            else:
                print('Usuário escolheu tesoura.')
                if comp == 1:
                    print('Computador escolheu pedra.')
                    user_wins=False
                else:
                    print('Computador escolheu papel.')
                    user_wins=True
            if (user_wins):
                print('Você venceu !!!')
            else:
                print('O computador venceu. Tente outra vez :(')
    else:
        print('Opção inválida!')
