from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel
from datetime import date


class TODO(BaseModel):
    title: str
    description: str
    date_added: str
    due_date: Optional[str] = None
