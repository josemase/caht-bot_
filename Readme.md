# 🤖 ChatBot Buy n Large

Un chatbot inteligente especializado en ventas de computadoras, desarrollado con Django y React.

## 🚀 Características

- 💬 Conversación natural y fluida  
- 📦 Información en tiempo real del inventario  
- 💻 Detalles técnicos de productos  
- 💰 Consulta de precios  
- 🎮 Recomendaciones para gaming  
- 🔍 Búsqueda por marca y especificaciones  

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados:

1. Python 3.8+  
2. Node.js 14+  
3. npm o Yarn  
4. Git  
## ⚙️ Instalación Paso a Paso
### 1. Backend (Django)

```bash
# 1. Crear la estructura de carpetas
mkdir chat_bot
cd chat_bot
mkdir back
cd back

# 2. Crear y activar el entorno virtual
python -m venv venv

# Windows: 
venv\Scripts\activate
# Linux/Mac: 
source venv/bin/activate

# 3. Instalar dependencias
pip install django==4.2 djangorestframework django-cors-headers

# 4. Crear proyecto Django
django-admin startproject back
cd back

# 5. Crear aplicaciones
python manage.py startapp chat_service
python manage.py startapp store_products

# 6. Crear estructura de carpetas
mkdir chat_service/data



