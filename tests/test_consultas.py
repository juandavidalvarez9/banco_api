def test_saldo_de_usuario_existente(client):
    respuesta = client.get("/user/balance/camilo24")

    assert respuesta.status_code == 200
    assert respuesta.json() == {"username": "camilo24", "balance": 120000}


def test_saldo_de_usuario_inexistente(client):
    respuesta = client.get("/user/balance/no_existe")

    assert respuesta.status_code == 404
    assert respuesta.json() == {"detail": "El usuario no existe."}


def test_auth_correcta(client):
    respuesta = client.post(
        "/user/auth/", json={"username": "camilo24", "password": "root"}
    )

    assert respuesta.json() == {"Autenticado": True}


def test_auth_clave_incorrecta(client):
    respuesta = client.post(
        "/user/auth/", json={"username": "camilo24", "password": "otra"}
    )

    assert respuesta.json() == {"Autenticado": False}


def test_auth_usuario_inexistente(client):
    respuesta = client.post(
        "/user/auth/", json={"username": "no_existe", "password": "x"}
    )

    assert respuesta.status_code == 404
