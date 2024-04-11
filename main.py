from fastapi import FastAPI, Response
from typing import Any
from orjson import orjson
import transactions
from mangum import Mangum
import todo


class CustomORJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed"
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)


app = FastAPI(default_response_class=CustomORJSONResponse)
handler = Mangum(app)


@app.get('/')
async def root():
    return {
        'transactions-commands': [
            'view',
            'add',
            'update',
            'delete']
    }

# Include Transactions API Router
app.include_router(transactions.router)
