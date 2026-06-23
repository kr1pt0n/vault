import sqlite3
import os
import jwt
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, HTTPException, status, Depends, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# =====================================================================
# CONFIGURACIÓN DE SEGURIDAD (Cámbialo a tu gusto)
# =====================================================================
SECRET_KEY = "SUPER_SECRET_VAULT_KEY_1337"  # Cambia esto por un string aleatorio
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 240  # El login dura 4 horas activo

ADMIN_USER = "admin"
ADMIN_PASS = "password"  # Pon aquí la contraseña que usarás para entrar
# =====================================================================

# 1. Automatización de rutas para Docker: Creamos la carpeta 'data' si no existe
os.makedirs("data", exist_ok=True)
DB_NAME = "data/vault.db"

def init_db():
    with sqlite3.connect(DB_NAME, timeout=20) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS commands ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "tipo TEXT, os TEXT, nombre TEXT, comando TEXT)"
        )
init_db()

class Command(BaseModel):
    tipo: str
    os: str
    nombre: str
    comando: str

# Herramienta de FastAPI para extraer el token Bearer automáticamente de las cabeceras HTTP
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

# FUNCIÓN DE VALIDACIÓN (Protege las rutas)
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username != ADMIN_USER:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token no válido")
        return username
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sesión expirada o token corrupto")

# ENDPOINT DE AUTENTICACIÓN (Recibe datos del formulario del HTML)
@app.post("/api/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == ADMIN_USER and password == ADMIN_PASS:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {"sub": username, "exp": expire}
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": encoded_jwt, "token_type": "bearer"}
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario o contraseña incorrectos")

# --- RUTAS DE LA API PROTEGIDAS (Añadido: Depends(get_current_user)) ---

@app.get("/api/commands")
def list_commands(current_user: str = Depends(get_current_user)):
    with sqlite3.connect(DB_NAME, timeout=20) as conn:
        conn.row_factory = sqlite3.Row
        return [dict(r) for r in conn.execute("SELECT * FROM commands").fetchall()]

@app.post("/api/commands")
def create(c: Command, current_user: str = Depends(get_current_user)):
    with sqlite3.connect(DB_NAME, timeout=20) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO commands (tipo, os, nombre, comando) VALUES (?,?,?,?)", (c.tipo, c.os, c.nombre, c.comando))
        conn.commit()
        return {"id": cur.lastrowid}

@app.delete("/api/commands/{id}")
def delete(id: int, current_user: str = Depends(get_current_user)):
    with sqlite3.connect(DB_NAME, timeout=20) as conn:
        conn.execute("DELETE FROM commands WHERE id = ?", (id,))
        conn.commit()
        return {"status": "ok"}

@app.put("/api/commands/{id}")
def update(id: int, c: Command, current_user: str = Depends(get_current_user)):
    with sqlite3.connect(DB_NAME, timeout=20) as conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE commands SET tipo = ?, os = ?, nombre = ?, comando = ? WHERE id = ?",
            (c.tipo, c.os, c.nombre, c.comando, id)
        )
        conn.commit()
        if cur.rowcount == 0:
            return {"status": "error", "message": "Comando no encontrado"}
        return {"status": "ok", "message": "Comando actualizado"}
        
@app.get("/")
def index(): 
    # Validación extra de seguridad para entornos de contenedores
    if not os.path.exists("index.html"):
        raise HTTPException(status_code=404, detail="Archivo index.html no encontrado en el contenedor")
    return FileResponse("index.html")
