import copy

import pytest
from fastapi.testclient import TestClient

import main
from db import transaction_db, user_db


@pytest.fixture(autouse=True)
def estado_limpio():
    """La base es en memoria: cada prueba arranca con los datos originales."""
    usuarios = copy.deepcopy(user_db.database_users)
    yield
    user_db.database_users.clear()
    user_db.database_users.update(usuarios)
    transaction_db.database_transactions.clear()
    transaction_db.generator["id"] = 0


@pytest.fixture
def client():
    return TestClient(main.api)
