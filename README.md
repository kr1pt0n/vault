# ⚡ VAULT - Red Team Command & Payload Manager

**VAULT** es un gestor local e interactivo diseñado para operadores de Red Team y pentesters. Permite centralizar, buscar, copiar, crear y editar payloads, exploits o comandos recurrentes organizados por categorías tácticas (Escaneo, Explotación, Persistencia, etc.) a través de una interfaz web minimalista con modo oscuro optimizado.

---

## 🚀 Características Claves

* 📂 **Organización Táctica:** Categorías predefinidas para cubrir las fases esenciales de una auditoría.
* 🔍 **Búsqueda Dinámica (Ctrl + K):** Filtrado en tiempo real por nombre del exploit o contenido del comando.
* 📝 **Gestión CRUD Completa:** Interfaz para crear, editar y eliminar comandos permanentemente desde el panel central.
* 📋 **Copiado Rápido:** Haz clic sobre cualquier bloque de código para copiar el payload directamente al portapapeles.
* 🗄️ **Backend Ligero:** Desarrollado con **FastAPI** y **SQLite**, optimizado contra bloqueos de concurrencia.

---

## 🛠️ Requisitos Previos

Antes de arrancar, asegúrate de tener instalado Python 3.8+ y las dependencias del proyecto:

```bash
sudo apt install python3-pip python3-venv python3-uvicorn python3-fastapi uvicorn
```
📦 Estructura del Proyecto
```bash
├── main.py          # Servidor Backend (FastAPI + SQLite)
├── index.html       # Interfaz de Usuario (HTML5, CSS3, JS Vanilla)
└── vault.db         # Base de datos local (Se genera automáticamente)
```
⚡ Instalación y Despliegue Local

[+] Clona este repositorio:
```bash
git clone [https://github.com/kr1pt0n/vault.git]
cd vault
```
[+] Inicia el servidor con Uvicorn:
```bash
uvicorn main:app --reload
```
[+] Accede desde tu navegador:
```bash
http://127.0.0.1:8000 en tu navegador preferido.
```
⌨️ Atajos de Teclado del Vault

Ctrl + K: Enfoca el cursor automáticamente en la barra de búsqueda lateral.

Esc: Cierra cualquier modal o formulario abierto de forma inmediata.

🔒 Nota de Seguridad / Descargo de Responsabilidad

    [!WARNING]
    Esta herramienta está diseñada exclusivamente para fines de investigación de seguridad, auditorías autorizadas y entornos de aprendizaje (CTFs/Laboratorios). El uso de payloads o comandos almacenados en este Vault contra objetivos sin consentimiento previo es totalmente ilegal. El desarrollador no se hace responsable del mal uso de este software.


