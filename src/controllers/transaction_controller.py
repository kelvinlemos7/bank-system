from services.transaction_service import TransactionService

class TransactionController:
    def __init__(self, service: TransactionService):
        self.service = service

    def create_transaction(self, account_id, amount, transaction_type, destination_account_id=None):
        return self.service.create_transaction(
            account_id,
            amount,
            transaction_type,
            destination_account_id
        )

    def get_transactions(self, account_id):
        return self.service.get_transactions(account_id)
