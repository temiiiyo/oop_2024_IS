from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    username: str
    role_id: int


@dataclass
class Transaction:
    transaction_id: int
    client_name: str
    currency_name: str
    amount: float
    total_in_rub: float
