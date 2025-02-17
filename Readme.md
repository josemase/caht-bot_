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
```
### 2. Configuración del Backend

1. Edita `back/settings.py`:
   
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'chat_service',
    'store_products',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

2. Crea el archivo `responses.json` en `chat_service/data/`.

3. Ejecuta las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Frontend (React)

```bash
# 1. Crear proyecto React
cd ../..
# Volver a la carpeta raíz
npm create vite@latest chat-bot -- --template react
cd chat-bot

# 2. Instalar dependencias
npm install

# 3. Crear estructura de carpetas
mkdir src/components
mkdir src/styles
```

## 🔧 Configuración de URLs

### Backend URLs (Django)

1. En `back/back/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat_service.views import ChatViewSet
from django.http import JsonResponse

def home(request):
    return JsonResponse({'status': 'ok', 'message': 'API funcionando'})

router = DefaultRouter()
router.register(r'chat', ChatViewSet, basename='chat')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
```

### Frontend URLs (React)

1. En `App.jsx`, configura la URL del backend:

```javascript
const BACKEND_URL = "http://127.0.0.1:8000";
const API_URL = `${BACKEND_URL}/api/chat/send_message/`;
```

## 🚀 Iniciar el Proyecto

### 1. Iniciar el Backend

```bash
cd back/back
python manage.py runserver
```

El backend estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 2. Iniciar el Frontend

```bash
cd chat-bot
npm run dev
```

El frontend estará disponible en: [http://localhost:5173](http://localhost:5173)

## 🤝 Probar el ChatBot

1. Abre [http://localhost:5173](http://localhost:5173) en tu navegador.
2. Haz preguntas como:
   - "Hola"
   - "¿Qué computadoras tienen?"
   - "Háblame sobre la MacBook Pro"
   - "¿Cuál es el precio de la Dell XPS?"

## 🔍 Verificación de Instalación

### Backend

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/) debería mostrar "API funcionando".
- [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) debería mostrar la documentación de la API.
- POST a [http://127.0.0.1:8000/api/chat/send_message/](http://127.0.0.1:8000/api/chat/send_message/) debería responder.

### Frontend

- [http://localhost:5173](http://localhost:5173) debería mostrar la interfaz del chat.
- La conexión con el backend debería funcionar sin errores CORS.
- Los mensajes deben enviarse y recibirse correctamente.

## ❗ Solución de Problemas Comunes

1. **Error CORS**:
   - Verifica que `corsheaders` está instalado y configurado.
   - Asegúrate de que el origen del frontend esté en `CORS_ALLOWED_ORIGINS`.

2. **Error "Module not found"**:
   - Verifica que todas las dependencias están instaladas.
   - Asegúrate de que las rutas de importación sean correctas.

3. **Error de conexión al backend**:
   - Verifica que ambos servidores (backend y frontend) estén corriendo.
   - Asegúrate de que las URLs sean correctas.

## 📞 Soporte

Si encuentras algún problema, sigue estos pasos:

1. Revisa los logs del servidor Django.
2. Revisa la consola del navegador.
3. Verifica que todas las dependencias estén instaladas.
4. Asegúrate de que los archivos estén en las ubicaciones correctas.

## 🔄 Actualizaciones

Para actualizar el proyecto:

```bash
# Backend
git pull
pip install -r requirements.txt
python manage.py migrate

# Frontend
git pull
npm install
```

## 🤝 Contribuir

1. Bifurca el proyecto.
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`).
3. Confirma tus cambios (`git commit -m 'Add some AmazingFeature'`).
4. Sube la rama (`git push origin feature/AmazingFeature`).
5. Abre un Pull Request.

## 📄 Licencia

Distribuido bajo la Licencia MIT. Ver `LICENCIA` para más información.

## 🎉 Agradecimientos

- Django REST Framework
- React Team
- Buy n Large por la oportunidad

**¡Gracias por usar el ChatBot Buy n Large!** 😊



