import base64
from fastapi.testclient import TestClient

from app.main import app, rsa

client = TestClient(app)
test_str = "Aa.  12!*$^"
valid_credentials = base64.b64encode(b"wielas:1234").decode("utf-8")


def test_cipher():
    encrypted_str = rsa.encrypt(test_str)
    assert encrypted_str == rsa.encrypt(''.join(rsa.decrypt(encrypted_str)))


def test_root():
    """ Test root endpoint """
    response = client.get("/", headers={"Authorization": "Basic " + valid_credentials})

    assert response.status_code == 200
    assert response.json()["username"] == "wielas"


def test_encryption():
    """ Test /encryption endpoint """
    response = client.get(f"/encrypt/{test_str}", headers={"Authorization": "Basic " + valid_credentials})

    assert response.status_code == 200
    assert response.json()["encrypted message"] == rsa.encrypt(test_str)


def test_decryption():
    """ Test /decryption endpoint """
    encrypted_str = rsa.encrypt(test_str)

    response = client.get(f"/decrypt/{encrypted_str}", headers={"Authorization": "Basic " + valid_credentials})

    assert response.status_code == 200
    assert response.json()["decrypted message"] == ''.join(rsa.decrypt(encrypted_str))
