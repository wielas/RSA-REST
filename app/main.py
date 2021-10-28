import json
import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app import RSA

app = FastAPI()
security = HTTPBasic()
rsa = RSA.RSA()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "wielas")
    correct_password = secrets.compare_digest(credentials.password, "1234")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/")
async def root(username: str = Depends(get_current_username)):
    return {
        "username": username,
    }


@app.get("/encrypt/{message}")
async def encrypt(message: str, username: str = Depends(get_current_username)):
    enc_mess = rsa.encrypt(message)
    return {"encrypted message": enc_mess}


@app.get("/decrypt/{encrypted_message}")
async def decrypt(encrypted_message: str, username: str = Depends(get_current_username)):
    dec_mess = ''.join(rsa.decrypt(json.loads(encrypted_message)))
    return {"decrypted message": dec_mess}
