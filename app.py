import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from controller import router
from schema import schema

graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
app.include_router(router, prefix="/v1")
