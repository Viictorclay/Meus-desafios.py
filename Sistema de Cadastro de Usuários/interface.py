import os
def menu():
    print('='*30)
    print('MENU'.center(30))
    print('='*30)
    print(' [1] Usuarios Cadastrados')
    print(' [2] Cadastrar Usuario')
    print(' [3] sair')
    print('='*30)
    try:
        option = int(input(' Digite: '))
        return option
    except:
        print('Por favor digite um valor valido.')
        return 0
        clear_system()
    

def clear_system():
    os.system('cls' if os.name == 'nt' else 'clear')