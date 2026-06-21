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
pip install fastapi uvicorn pydantic

📦 Estructura del Proyecto
Plaintext

├── main.py          # Servidor Backend (FastAPI + SQLite)
├── index.html       # Interfaz de Usuario (HTML5, CSS3, JS Vanilla)
└── vault.db         # Base de datos local (Se genera automáticamente)

⚡ Instalación y Despliegue Local

    Clona este repositorio:
    Bash

    git clone [https://github.com/TU_USUARIO/vault-redteam.git](https://github.com/TU_USUARIO/vault-redteam.git)
    cd vault-redteam

    Inicia el servidor con Uvicorn:
    Bash

    uvicorn main:app --reload

    Accede desde tu navegador:
    Abre http://127.0.0.1:8000 en tu navegador preferido.

⌨️ Atajos de Teclado del Vault

    Ctrl + K: Enfoca el cursor automáticamente en la barra de búsqueda lateral.

    Esc: Cierra cualquier modal o formulario abierto de forma inmediata.

🔒 Nota de Seguridad / Descargo de Responsabilidad

    [!WARNING]
    Esta herramienta está diseñada exclusivamente para fines de investigación de seguridad, auditorías autorizadas y entornos de aprendizaje (CTFs/Laboratorios). El uso de payloads o comandos almacenados en este Vault contra objetivos sin consentimiento previo es totalmente ilegal. El desarrollador no se hace responsable del mal uso de este software.


### 💡 Tips antes de subirlo a GitHub:
1. Recuerda cambiar `TU_USUARIO` en la sección de clonado por tu nombre real de GitHub.
2. **Recomendación:** Crea un archivo llamado `.gitignore` en la misma carpeta y escribe adentro `vault.db`. De esta forma, tu base de datos personal con tus payloads locales no se subirá públicamente a internet y mantendrás limpio el repositorio para que otros generen su propia base de datos desde cero. 

¡Ya lo tienes listo para presumir en tu perfil! 🚀
