from interface import menu, clear_system
from arquivo import listar, cadastrar

while True:
    option = menu()
    if option == 1:
        clear_system()
        listar()
    elif option == 2:
        clear_system()
        nome = input(' Nome: ')
        idade = input(' Idade: ')
        cadastrar(nome, idade)
    elif option == 3:
        print('Até a proxima.')
        break
    else:
        clear_system()
        print('Opção inválida, tente novamente.')