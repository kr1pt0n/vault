<div align="center">
  <br />
      <img src="https://i.ibb.co/fYTqqB19/s2.jpg" alt="Project Banner">
  <br />

<div>
  <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logoColor=white&logo=python&color=3776AB" alt="python" />
  <img src="https://img.shields.io/badge/-FastAPI-black?style=for-the-badge&logoColor=white&logo=fastapi&color=009688" alt="fastapi" />
  <img src="https://img.shields.io/badge/-SQLite-black?style=for-the-badge&logoColor=white&logo=sqlite&color=003B57" alt="sqlite" />
  <img src="https://img.shields.io/badge/-HTML5-black?style=for-the-badge&logoColor=white&logo=html5&color=E34F26" alt="html5" />
  <img src="https://img.shields.io/badge/-CSS3-black?style=for-the-badge&logoColor=white&logo=css3&color=1572B6" alt="css3" />
  <img src="https://img.shields.io/badge/-JavaScript-black?style=for-the-badge&logoColor=white&logo=javascript&color=F7DF1E" alt="javascript" />
</div>
</div>
<h3 align="center">⚡ VAULT - Red Team Command & Payload Manager</h3>

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
git clone https://github.com/kr1pt0n/vault.git
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


