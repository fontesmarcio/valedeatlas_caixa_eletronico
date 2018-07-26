from Cash_Machine_Modules.cash_machine import CashMachineWithdraw, CashMachineInsertMoneyBills, \
    CashMachineDepositMoneyAccount
from Cash_Machine_Modules.cash_machine_auth import AuthBankAccount



class CashMachineOperations:
    OPERATION_SHOW_BALANCE = '1'
    OPERATION_WITHDRAW = '2'
    OPERATION_DEPOSIT = '3'
    OPERATION_INSERT_MONEY_BILL = '4'

    @staticmethod
    def do_operations(option):
        bank_account = AuthBankAccount.bank_account_authenticated
        if option == CashMachineOperations.OPERATION_SHOW_BALANCE:
            ShowBalanceOperation.do_operation()
        elif option == CashMachineOperations.OPERATION_WITHDRAW:
            WithdrawOperation.do_operation()
        elif option == CashMachineOperations.OPERATION_DEPOSIT:
            DepositOperation.do_operation()
        elif option == CashMachineOperations.OPERATION_INSERT_MONEY_BILL and bank_account.admin:
            InsertMoneyBillOperation.do_operation()
        else:
            print('\nOpção Inválida')


class ShowBalanceOperation:
    @staticmethod
    def do_operation():
        bank_account = AuthBankAccount.bank_account_authenticated
        print(f"\nSeu saldo é {bank_account.value}")


class WithdrawOperation:
    @staticmethod
    def do_operation():
        value_typed = input('\nDigite o valor a ser sacado: ')
        value_int = int(value_typed)
        bank_account = AuthBankAccount.bank_account_authenticated

        if value_int > bank_account.value:
            print('\nSaldo insuficiente. Consulte seu saldo e tente realizar novamente a operação')
        else:
            cash_machine = CashMachineWithdraw.withdraw(bank_account, value_int)
            if cash_machine.value_remaining != 0:
                print('\nO caixa não tem cédulas disponiveis para este valor')
            else:
                print('\nPegue as notas: ')
                print(cash_machine.money_slips_user)
                print(f"\nSeu saldo é: {bank_account.value}")


class DepositOperation:
    @staticmethod
    def do_operation():
        bank_account = AuthBankAccount.bank_account_authenticated
        deposit_amount = float(input('\nDigite a quantidade a ser depositada: '))
        CashMachineDepositMoneyAccount.balance_deposit(bank_account, deposit_amount)
        print(f"\nSeu novo saldo é: {bank_account.value}")


class InsertMoneyBillOperation:
    @staticmethod
    def do_operation():
        amount_typed = int(input('\nDigite a quantidade de cédulas: '))
        money_bill_typed = input('\nDigite a cédula a ser incluída(10,20,50 ou 100): ')
        cash_machine = CashMachineInsertMoneyBills.insert_money_bill(money_bill_typed, int(amount_typed))
        print(cash_machine)
