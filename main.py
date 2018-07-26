from utils import clear_screen, header, pause
from Cash_Machine_Modules.cash_machine_console import CashMachineConsole, AuthBankAccountConsole


def main():
    clear_screen()
    header()

    if AuthBankAccountConsole.is_auth():
        clear_screen()
        header()
        CashMachineConsole.call_operation()
    else:
        print('\nConta inválida!')


if __name__ == '__main__':
    while True:
        main()
        pause()
