def listar():
    try:
        with open('cadastro.txt','r') as arquivo:
            print('='* 30)
            print(' PESSOAS CADASTRADAS'.center(30))
            print('='*30)
            for linha in arquivo:
                print(linha.strip())
    except FileNotFoundError:
        print(' Ainda não há cadastros.')
    
def cadastrar(nome,idade):
    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(f'{nome};{idade}\n')
    print(f'Cadastro de {nome} adcicionado com sucesso!')
    