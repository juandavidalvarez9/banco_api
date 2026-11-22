# banco_api

> **Estado:** proyecto de 2020, sin mantenimiento. Se conserva como archivo.

API de ejemplo de un banco, hecha con FastAPI. Usa una base de datos ficticia en memoria (los usuarios y saldos son datos de prueba y se reinician al reiniciar el servidor).

## Qué hace

| Método | Ruta | Descripción |
|---|---|---|
| `POST` | `/user/auth/` | Valida usuario y contraseña |
| `GET` | `/user/balance/{username}` | Consulta el saldo de un usuario |
| `PUT` | `/user/transaction/` | Registra un retiro y devuelve el saldo actualizado |

## Cómo ejecutarla

```bash
pip install -r requirements.txt
uvicorn main:api --reload
```

La documentación interactiva queda en `http://127.0.0.1:8000/docs`.

## Relacionado
- [Banco](https://github.com/juandavidalvarez9/Banco): interfaz en Vue.js que consume esta API.

## Licencia
Ver [LICENSE](LICENSE).
