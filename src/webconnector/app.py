from fastapi import FastAPI

from webconnector.routers import test_connection, describe_collections, execute_query

app = FastAPI(title="Crystal WebConnector Datasource Adapter")

app.include_router(test_connection.router, tags=["crystal endpoints"])
app.include_router(describe_collections.router, tags=["crystal endpoints"])
app.include_router(execute_query.router, tags=["crystal endpoints"])