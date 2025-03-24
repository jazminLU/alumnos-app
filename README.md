# 📋 Alumnos App - Docker Fullstack

Aplicación web simple para registrar y consultar alumnos.  
Basada en una arquitectura de microservicios con:

- 🎨 Frontend en HTML/CSS/JS servido por NGINX
- 🧠 Backend REST en Flask (Python)
- 🗃️ Base de datos PostgreSQL
- 📘 Documentación con Swagger (via Flask-RestX)

---

## 🚀 ¿Qué hace esta app?

- Permite agregar alumnos por nombre usando un formulario
- Lista todos los alumnos registrados
- Guarda los datos en una base de datos PostgreSQL
- Expone una API REST con Swagger (`/docs`)

---

## ⚙️ Requisitos

- Docker
- Docker Compose

---

## 🛠️ Cómo levantar el proyecto

1. Cloná el repo o descargá el ZIP
2. Desde la raíz del proyecto:

```bash
docker-compose up --build
```
