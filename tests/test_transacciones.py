import time

from db import transaction_db


def retirar(client, valor, usuario="camilo24"):
    return client.put(
        "/user/transaction/", json={"username": usuario, "value": valor}
    )


def saldo(client, usuario="camilo24"):
    return client.get(f"/user/balance/{usuario}").json()["balance"]


def test_cada_retiro_recibe_un_id_consecutivo(client):
    primero = retirar(client, 1000)
    segundo = retirar(client, 1000)

    assert primero.json()["id_transaction"] == 1
    assert segundo.json()["id_transaction"] == 2
    assert len(transaction_db.database_transactions) == 2


def test_cada_transaccion_tiene_su_propia_fecha():
    primera = transaction_db.TransactionInDB(
        username="camilo24", value=1, actual_balance=1
    )
    time.sleep(0.01)
    segunda = transaction_db.TransactionInDB(
        username="camilo24", value=1, actual_balance=1
    )

    assert segunda.date > primera.date
    assert primera.date.tzinfo is not None
