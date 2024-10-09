#![image](https://github.com/user-attachments/assets/43a46a7c-2931-4098-9048-2457be181c88)

# Sistema de Gerenciamento de Restaurantes

Este projeto é um sistema de gerenciamento de restaurantes desenvolvido em Python. O objetivo principal é permitir o cadastro, listagem e alteração do status de restaurantes em um menu interativo no console.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada para desenvolver a aplicação.
- **JSON**: Estrutura de dados utilizada para armazenar as informações dos restaurantes.
- **ASCII Art**: Utilizado para estilizar a interface do console.

## Funcionalidades

- **Cadastrar Restaurante**: Permite ao usuário adicionar novos restaurantes ao sistema.
- **Listar Restaurantes**: Exibe uma lista dos restaurantes cadastrados com suas respectivas categorias e status (ativado/desativado).
- **Alternar Status de Restaurante**: Altera o status de um restaurante, permitindo ativá-lo ou desativá-lo.

## Estrutura do Código

O arquivo principal do projeto é `app.py`, que contém as seguintes funções:

- `exibir_nome_do_programa()`: Exibe o título do programa em formato ASCII.
- `exibir_opcoes()`: Mostra as opções disponíveis no menu principal.
- `finalizar_app()`: Exibe uma mensagem de finalização do aplicativo.
- `voltar_ao_menu_principal()`: Retorna ao menu principal.
- `opcao_invalida()`: Notifica o usuário sobre uma opção inválida.
- `exibir_subtitulo(texto)`: Exibe subtítulos estilizados no console.
- `cadastrar_novos_restaurantes()`: Permite o cadastro de novos restaurantes.
- `listar_restaurantes()`: Lista os restaurantes cadastrados.
- `alternar_estado_do_restaurante()`: Alterna o estado de um restaurante entre ativado e desativado.
- `escolher_opcao()`: Permite ao usuário escolher uma opção do menu.
- `main()`: Função principal que inicia o programa.

## Como Executar

1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone o repositório ou baixe o arquivo `app.py`.
3. Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo `app.py` está localizado.
4. Execute o seguinte comando:

   ```bash
   python app.py
