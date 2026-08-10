from decimal import Decimal
from sqlalchemy.orm import Session
from repositories.transaction_repository import TransactionRepository
from repositories.account_repository import AccountRepository
from models.transaction import Transaction
from utils.validators import validate_positive_value
from utils.errors import AccountNotFoundError, InsufficientBalanceError, BusinessError
from utils.enum import TransactionType


class TransactionService:
    def __init__(
        self,
        db: Session,
        transaction_repository: TransactionRepository,
        account_repository: AccountRepository
    ):
        self.db = db
        self.transaction_repository = transaction_repository
        self.account_repository = account_repository

    def create_transaction(
        self,
        account_id: int,
        amount: float,
        transaction_type: TransactionType,
        destination_account_id: int | None = None
    ):
        try:
            validate_positive_value(amount)
            amount_decimal = Decimal(str(amount))

            account = self.account_repository.get_by_id_for_update(account_id)
            if not account:
                raise AccountNotFoundError("Conta não encontrada")

            destination = None
            if transaction_type == TransactionType.TRANSFER:
                if not destination_account_id:
                    raise AccountNotFoundError("Conta de destino obrigatória")
                if destination_account_id == account_id:
                    raise BusinessError("Transferência para a própria conta não permitida")

                destination = self.account_repository.get_by_id_for_update(destination_account_id)
                if not destination:
                    raise AccountNotFoundError("Conta de destino não encontrada")

            if transaction_type in [TransactionType.WITHDRAW, TransactionType.TRANSFER]:
                if account.balance < amount_decimal:
                    raise InsufficientBalanceError("Saldo insuficiente")

            if transaction_type == TransactionType.DEPOSIT:
                account.balance += amount_decimal

            elif transaction_type == TransactionType.WITHDRAW:
                account.balance -= amount_decimal

            elif transaction_type == TransactionType.TRANSFER:
                account.balance -= amount_decimal
                destination.balance += amount_decimal
                self.db.add(destination)

            self.db.add(account)

            transaction = Transaction(
                account_id=account.id,
                amount=amount_decimal,
                transaction_type=transaction_type.value,
                destination_account_id=destination.id if destination else None
            )

            self.db.add(transaction)

            self.db.commit()

            self.db.refresh(transaction)
            return transaction

        except Exception:
            self.db.rollback()
            raise

    def get_transactions(self, account_id: int):
        return self.transaction_repository.get_by_account(account_id)
