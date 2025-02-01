import enum
import datetime


class OpTypes(enum.Enum):
    DEPOSITE = "deposite"
    WITHDRAWAL = "withdrawal"


class Operation:

    def __init__(self, name: str, amount: float, operation_type: str) -> None:
        self.name = name
        self.amount = amount
        self.operation_type = operation_type
        self.date = datetime.datetime.now().timestamp()

    def __str__(self) -> str:
        date = datetime.datetime.fromtimestamp(self.date).strftime('%H:%M:%S %d/%m/%Y')
        return f"Operation: {date} {self.operation_type} of {self.amount} from the account {self.name}"


class Account:

    def __init__(
        self,
        name: str,
        balance: float
    ) -> None:
        self.name = name
        self.balance = balance
        self.operations = []

    def deposite(self, amount: float) -> None:
        self.balance += amount
        self._log_deposite(amount)

    def withdrawal(self, amount: float) -> None:
        self.balance -= amount
        self._log_withdrawal(amount)

    def _log_operation(self, amount: float, operation_type: str) -> None:
        t = Operation(self.name, amount, operation_type)
        self.operations.append(t)

    def _log_deposite(self, amount: float) -> None:
        self._log_operation(amount, OpTypes.DEPOSITE.value)

    def _log_withdrawal(self, amount: float) -> None:
        self._log_operation(amount, OpTypes.WITHDRAWAL.value)

    def print_account_info(self) -> None:
        print(self.__str__())

    def print_operation_history(self) -> None:
        for op in self.operations:
            print(op.__str__())

    def __str__(self) -> str:
        return f"Account \"{self.name}\": {self.balance}"


def main():
    a1 = Account("Petya", 200)
    a2 = Account("Oleg", 100)

    a1.print_account_info()
    a1.deposite(50)
    a1.deposite(15)
    a1.withdrawal(135)
    a1.print_operation_history()
    a1.print_account_info()

    a2.print_account_info()
    a2.withdrawal(40)
    a2.deposite(200)
    a2.withdrawal(110)
    a2.print_operation_history()
    a2.print_account_info()


main()
