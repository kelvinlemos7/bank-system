from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from controllers.transaction_controller import TransactionController
from repositories.transaction_repository import TransactionRepository
from repositories.account_repository import AccountRepository
from services.transaction_service import TransactionService
from utils.enum import TransactionType

router = APIRouter(prefix="/transactions", tags=["Transactions"])


def _build_controller(db: Session) -> TransactionController:
    transaction_repo = TransactionRepository(db)
    account_repo = AccountRepository(db)
    service = TransactionService(
        db=db,
        transaction_repository=transaction_repo,
        account_repository=account_repo
    )
    return TransactionController(service)


@router.post("/")
def create_transaction(
    account_id: int,
    amount: float,
    transaction_type: TransactionType,
    destination_account_id: int | None = None,
    db: Session = Depends(get_db)
):
    return _build_controller(db).create_transaction(
        account_id=account_id,
        amount=amount,
        transaction_type=transaction_type,
        destination_account_id=destination_account_id
    )

@router.get("/accounts/{account_id}/transactions")
def get_transactions(
    account_id: int,
    db: Session = Depends(get_db)
):
    return _build_controller(db).get_transactions(account_id)

