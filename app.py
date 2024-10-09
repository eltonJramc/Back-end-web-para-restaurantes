import os

restaurantes = [{'Nome':'Praça', 'Categoria':'Japonesa', 'Ativo':False},
                {'Nome':'Pizza Suprema', 'Categoria':'Italiana', 'Ativo':True},
                {'Nome':'Cantina', 'Categoria':'Italiana', 'Ativo':False}]

def exibir_nome_do_programa():
    '''Essa função é responsável por extilizar o título do programa em execução. Foi utilizado a arte ASCII.'''

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    '''Essa função é responsável por exibir no menu principal as opções de saída para o usuário.'''

    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar Status de Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função é responsável por exibir uma mensagem ao finalizar o aplicativo'''

    exibir_subtitulo('Finalizando o app!\n')

def voltar_ao_menu_principal():
    '''Solicita uma tecla para voltar ao menu principal.
    
    Outputs:
    - Retorna ao menu principal'''

    input('\nAperte qualquer tecla para voltar ao menu principal: \n')
    main()

def opcao_invalida():
    '''Exibe mensagem de opção inválida e retorna ao menu principal.
    
    Outputs:
    - Retorna ao menu principal'''

    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Exibe um subtítulo entre os títulos para poder extilizar
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def cadastrar_novos_restaurantes():
     '''Essa função é responsável por cadastrar um novo restaurante
     
     Inputs: 
     - Nome do restaurante
     - Categoria

     Outputs:
     - Adiciona um novo restaurante a lista d erestaurantes. 
     '''
     exibir_subtitulo('Cadastro de novos restaurantes')
     nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
     categoria = input(f'Digite o nome da categoria desse restaurante {nome_do_restaurante}: ')
     dados_dos_restaurantes = {'Nome': nome_do_restaurante, 'Categoria': categoria, 'Ativo':False}
     restaurantes.append(dados_dos_restaurantes)
     print(f'O restaurante {nome_do_restaurante} foi adiconado com sucesso!\n')
     voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função exibe as listas de restaurantes presentes na lista.
    
    outputs:
    - Exibe a lista de restaurante na tela com esses títulos: Nome, categoria e status do restaurante. 
    '''
    exibir_subtitulo('Lista de restaurantes\n')
    print(f'{'Lista de Restaurantes'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = 'Ativado' if restaurante['Ativo'] else 'desativado'
        print(f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    '''Altera o estado ativo/desativado de um restaurante.
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação.
    '''
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''Essa função tem o propósito de disponibilizar o menu principal e apartir disso o usuário fazer uma escolha
    
    Input:
    - Escolher uma opção do menu disponível

    Outputs:
    - Mostrar as opções disponíveis no menu. 
    - Caso o usuário escolha algo não disponível, o programa irá mostrar uma mensagem de invalidez. 
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        #opcao_escolhida = int(opcao_escolhida)

        #print('Você escolheu a opção', opcao_escolhida) - Uma forma mais boa prática:
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novos_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()