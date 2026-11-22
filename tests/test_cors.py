ORIGEN_DEL_FRONT = "http://localhost:5173"


def test_origen_permitido_recibe_cabecera_cors(client):
    respuesta = client.get(
        "/user/balance/camilo24", headers={"Origin": ORIGEN_DEL_FRONT}
    )

    assert respuesta.headers["access-control-allow-origin"] == ORIGEN_DEL_FRONT


def test_preflight_de_retiro_desde_origen_permitido(client):
    respuesta = client.options(
        "/user/transaction/",
        headers={
            "Origin": ORIGEN_DEL_FRONT,
            "Access-Control-Request-Method": "PUT",
            "Access-Control-Request-Headers": "content-type",
        },
    )

    assert respuesta.status_code == 200
    assert "PUT" in respuesta.headers["access-control-allow-methods"]


def test_origen_no_permitido_no_recibe_cabecera(client):
    respuesta = client.get(
        "/user/balance/camilo24", headers={"Origin": "http://malo.example"}
    )

    assert "access-control-allow-origin" not in respuesta.headers
