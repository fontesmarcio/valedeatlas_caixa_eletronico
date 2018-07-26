import getpass

from Cash_Machine_Modules.cash_machine_auth import AuthBankAccount
from Cash_Machine_Modules.cash_machine_operations import CashMachineOperations


class AuthBankAccountConsole:

    @staticmethod
    def is_auth():
        account_number = input('\nDigite sua conta: ')
        password_typed = getpass.getpass('\nDigite a sua senha: ')

        return AuthBankAccount.authenticate(account_number, password_typed)


class CashMachineConsole:

    @staticmethod
    def call_operation():
        option_typed = CashMachineConsole.__get_menu_options_typed()
        CashMachineOperations.do_operations(option_typed)

    @staticmethod
    def __get_menu_options_typed():
        bank_account = AuthBankAccount.bank_account_authenticated
        print('%s - Saldo' % CashMachineOperations.OPERATION_SHOW_BALANCE)
        print('%s - Saque' % CashMachineOperations.OPERATION_WITHDRAW)
        print('%s - Depósito' % CashMachineOperations.OPERATION_DEPOSIT)
        if bank_account.admin:
            print('%s - Inserir Cédulas' % CashMachineOperations.OPERATION_INSERT_MONEY_BILL)
        return input('\nEscolha uma das opções: ')
