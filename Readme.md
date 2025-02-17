# 🤖 ChatBot Buy n Large

Un chatbot inteligente especializado en ventas de computadoras, desarrollado con Django + React.

## 🚀 Características

- 💬 Conversación natural y fluida
- 📦 Información en tiempo real del inventario
- 💻 Detalles técnicos de productos
- 💰 Consulta de precios
- 🎮 Recomendaciones para gaming
- 🔍 Búsqueda por marca y especificaciones

## 📋 Requisitos Previos

1. Python 3.8+
2. Node.js 14+
3. npm o yarn
4. Git

## ⚙️ Instalación Paso a Paso

### 1. Backend (Django)

```bash
# 1. Crear la estructura de carpetas
mkdir chat_bot
cd chat_bot
mkdir back
cd back

# 2. Crear y activar entorno virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install django==4.2
pip install djangorestframework
pip install django-cors-headers

# 4. Crear proyecto Django
django-admin startproject back
cd back

# 5. Crear aplicación
python manage.py startapp chat_service
python manage.py startapp store_products

# 6. Crear estructura de archivos
mkdir chat_service/data
```

### 2. Configuración del Backend

1. Editar `back/settings.py`:

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

2. Crear archivo `responses.json` en `chat_service/data/`

3. Ejecutar migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Frontend (React)

```bash
# 1. Crear proyecto React
cd ../..  # Volver a la carpeta raíz
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
    return JsonResponse({
        'status': 'ok',
        'message': 'API funcionando'
    })

router = DefaultRouter()
router.register(r'chat', ChatViewSet, basename='chat')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
```

### Frontend URLs (React)

1. En `App.jsx`, configurar la URL del backend:

```javascript
const BACKEND_URL = "http://127.0.0.1:8000";
const API_URL = `${BACKEND_URL}/api/chat/send_message/`;
```

## 🚀 Iniciar el Proyecto

1. Iniciar el Backend:

```bash
cd back/back
python manage.py runserver
```

El backend estará disponible en: http://127.0.0.1:8000

2. Iniciar el Frontend:

```bash
cd chat-bot
npm run dev
```

El frontend estará disponible en: http://localhost:5173

## 🤝 Probar el ChatBot

1. Abrir http://localhost:5173 en el navegador
2. Hacer preguntas como:
   - "Hola"
   - "¿Qué computadoras tienen?"
   - "Háblame sobre la MacBook Pro"
   - "¿Cuál es el precio de la Dell XPS?"

## 🔍 Verificación de Instalación

### Backend

- http://127.0.0.1:8000/ debería mostrar "API funcionando"
- http://127.0.0.1:8000/api/ debería mostrar la documentación de la API
- POST a http://127.0.0.1:8000/api/chat/send_message/ debería responder

### Frontend

- http://localhost:5173 debería mostrar la interfaz del chat
- La conexión con el backend debería funcionar sin errores CORS
- Los mensajes deberían enviarse y recibirse correctamente

## ❗ Solución de Problemas Comunes

1. Error CORS:

   - Verificar que `corsheaders` está instalado y configurado
   - Comprobar que el origen del frontend está en `CORS_ALLOWED_ORIGINS`

2. Error "Module not found":

   - Verificar que todas las dependencias están instaladas
   - Comprobar que las rutas de importación son correctas

3. Error de conexión al backend:
   - Verificar que ambos servidores están corriendo
   - Comprobar que las URLs son correctas

## 📞 Soporte

Si encuentras algún problema:

1. Revisa los logs del servidor Django
2. Revisa la consola del navegador
3. Verifica que todas las dependencias están instaladas
4. Comprueba que los archivos están en las ubicaciones correctas

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

## 🤝 Uso

1. Inicia ambos servidores (backend en puerto 8000, frontend en 5173)
2. Abre http://localhost:5173 en tu navegador
3. ¡Comienza a chatear!

### Ejemplos de Preguntas

```plaintext
- "¿Qué computadoras tienen disponibles?"
- "Háblame sobre la MacBook Pro"
- "¿Cuál es la mejor computadora para gaming?"
- "¿Tienen laptops HP?"
- "¿Cuál es el precio de la Dell XPS?"
```

## 🎯 Endpoints API

- `GET /`: Información general de la API
- `GET /api/`: Lista de endpoints disponibles
- `POST /api/chat/send_message/`: Enviar mensaje al chatbot

### Ejemplo de Petición

```json
POST /api/chat/send_message/
{
    "message": "¿Qué computadoras tienen?",
    "conversation_id": null
}
```

### Ejemplo de Respuesta

```json
{
  "response": "Actualmente tenemos 4 computadoras disponibles:\n• 2 laptops HP\n• 1 laptop Dell\n• 1 MacBook Pro\n¿Te gustaría saber más sobre alguna en particular? 💻",
  "timestamp": "2024-02-16T01:48:48.123456Z",
  "conversation_id": "123"
}
```

## 📝 Estructura del Proyecto

```
chatbot/
├── back/
│   └── back/
│       ├── chat_service/
│       │   ├── data/
│       │   │   └── responses.json
│       │   ├── migrations/
│       │   ├── models.py
│       │   ├── serializers.py
│       │   └── views.py
│       └── back/
│           ├── settings.py
│           └── urls.py
└── chat-bot/
    ├── src/
    │   ├── components/
    │   ├── styles/
    │   ├── App.jsx
    │   └── main.jsx
    └── package.json
```

## 👥 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## 🎉 Agradecimientos

- Django REST Framework
- React Team
- Buy n Large por la oportunidad
#   C h a t _ B o t  
 