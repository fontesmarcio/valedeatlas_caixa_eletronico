import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


# Função para criar um cabeçalho
def header():
    print("*" * 54)
    print("********** Atlas Valley  - Caixa Eletrônico **********")
    print("*" * 54)


# Função para limpar a tela dependendo do sitema operacional
# nt = windows
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    input('\nPressione <ENTER> para continuar...')
