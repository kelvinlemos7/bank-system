from fastapi import FastAPI
from fastapi.responses import JSONResponse

from utils.errors import (
    UserNotFoundError,
    AccountNotFoundError,
    InsufficientBalanceError,
    BusinessError,
    DuplicateUserError,
    InvalidTransactionError,
    InvalidEmailError,
    InvalidNameError,
    InvalidValueError,
)

_STATUS_CODES = {
    UserNotFoundError: 404,
    AccountNotFoundError: 404,
    InsufficientBalanceError: 400,
    BusinessError: 400,
    DuplicateUserError: 409,
    InvalidTransactionError: 400,
    InvalidEmailError: 422,
    InvalidNameError: 422,
    InvalidValueError: 422,
}


def register_exception_handlers(app: FastAPI) -> None:
    for error_class, status_code in _STATUS_CODES.items():
        app.add_exception_handler(
            error_class,
            lambda request, exc, _code=status_code: JSONResponse(
                status_code=_code,
                content={"detail": str(exc)},
            ),
        )
