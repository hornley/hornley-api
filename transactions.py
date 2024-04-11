from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel
from datetime import date


class Transaction(BaseModel):
    name: str
    type: str
    date: str
    amount: float
    description: str
    transaction_name: Optional[str] = None
    date_added: Optional[str] = None


router = APIRouter()
transactions = {}


@router.post('/transactions/add')
async def add_transaction(transaction: Transaction):
    transaction_id = 0
    while transaction_id in transactions.keys():
        transaction_id += 1
    transaction.date_added = date.today()
    transactions[transaction_id] = transaction
    return transactions[transaction_id]


@router.put('/transactions/update/{transaction_id}')
async def update_transaction(transaction_id: int, transaction: Transaction):
    if transaction_id not in transactions:
        return {"ValueError": "Transaction ID does not exist!"}
    transactions[transaction_id].update(transaction)
    return transactions[transaction_id]


@router.delete('/transactions/delete/{transaction_id}')
async def delete_transaction(transaction_id: int):
    if transaction_id not in transactions:
        return {"ValueError": "Transaction ID does not exist!"}
    del transactions[transaction_id]
    return f"Successfully deleted '{transaction_id}'"


@router.get('/transactions/view/')
async def read_transaction(id: str = None, name: str = None):
    if id is not None:
        if id in transactions.keys():
            return transactions[id]
        return {"ValueError": "Transaction ID does not exist!"}

    if name is not None:
        for k, v in transactions.items():
            if name == v.name:
                return transactions[k]
        return {"ValueError": "Transaction name does not exist!"}

    return {"MissingParameters": "Neither an id or transaction name was provided!"}


@router.get('/transactions/', response_class=JSONResponse)
async def read_transactions():
    return transactions
