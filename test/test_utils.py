import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from odmantic import SyncEngine
from pymongo import MongoClient
from controller import router


@pytest.fixture
def client_fixture():
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


@pytest.fixture
def mongo_fixture():
    client = MongoClient("mongodb://localhost:27017/")
    engine = SyncEngine(client=client, database="customer_db")
    return engine
