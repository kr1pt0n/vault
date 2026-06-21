import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
DB_NAME = "vault.db"

def init_db():
    with sqlite3.connect(DB_NAME, timeout=20) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS commands (id INTEGER PRIMARY KEY AUTOINCREMENT, tipo TEXT, os TEXT, nombre TEXT, comando TEXT)")
init_db()

class Command(BaseModel):
    tipo: str
    os: str
    nombre: str
    comando: str

@app.get("/api/commands")
def list_commands():
    with sqlite3.connect(DB_NAME, timeout=20) as conn:
        conn.row_factory = sqlite3.Row
        return [dict(r) for r in conn.execute("SELECT * FROM commands").fetchall()]

@app.post("/api/commands")
def create(c: Command):
    with sqlite3.connect(DB_NAME, timeout=20) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO commands (tipo, os, nombre, comando) VALUES (?,?,?,?)", (c.tipo, c.os, c.nombre, c.comando))
        conn.commit()
        return {"id": cur.lastrowid}

@app.delete("/api/commands/{id}")
def delete(id: int):
    with sqlite3.connect(DB_NAME, timeout=20) as conn:
        conn.execute("DELETE FROM commands WHERE id = ?", (id,))
        conn.commit()
        return {"status": "ok"}

@app.put("/api/commands/{id}")
def update(id: int, c: Command):
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
def index(): return FileResponse("index.html")
