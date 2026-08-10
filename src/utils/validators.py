from utils.errors import InvalidEmailError, InvalidNameError, InvalidValueError

def validate_positive_value(value: float):
    if value <= 0:
        raise InvalidValueError("Valor deve ser maior que zero")

def validate_non_negative_value(value: float):
    if value < 0:
        raise InvalidValueError("Valor não pode ser negativo")
    
def validate_email(email: str):
    if "@" not in email:
        raise InvalidEmailError("Email inválido")
    
def validate_name(name: str):
    if name.strip() == "":
        raise InvalidNameError("Nome inválido")
