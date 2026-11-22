from pydantic import BaseModel, Field
from datetime import datetime

class TransactionIn(BaseModel):
    username: str
    value: int = Field(gt=0)

class TransactionOut(BaseModel):
    id_transaction: int
    username: str
    date: datetime
    value: int
    actual_balance: int