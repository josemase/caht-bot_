import json
import random
import os
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ChatViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            # Cargar el archivo JSON
            json_path = os.path.join(os.path.dirname(__file__), 'data', 'responses.json')
            with open(json_path, 'r', encoding='utf-8') as f:
                self.responses = json.load(f)
        except Exception as e:
            print(f"Error al cargar responses.json: {e}")
            self.responses = {
                "respuestas_generales": {
                    "no_entiendo": ["Lo siento, ha ocurrido un error al cargar las respuestas."]
                }
            }

    @action(detail=False, methods=['post'])
    def send_message(self, request):
        try:
            message = request.data.get('message', '').lower()
            conversation_id = request.data.get('conversation_id')

            # Crear o obtener conversación
            if conversation_id:
                conversation = Conversation.objects.get(id=conversation_id)
            else:
                conversation = Conversation.objects.create(user=request.user if request.user.is_authenticated else None)

            # Guardar mensaje del usuario
            Message.objects.create(
                conversation=conversation,
                content=message,
                is_user=True
            )

            # Procesar el mensaje y obtener respuesta
            response_text = self.process_message(message)

            # Guardar respuesta del bot
            bot_message = Message.objects.create(
                conversation=conversation,
                content=response_text,
                is_user=False
            )

            return Response({
                'response': response_text,
                'timestamp': bot_message.timestamp,
                'conversation_id': conversation.id
            })
        except Exception as e:
            print(f"Error en send_message: {e}")
            return Response({
                'response': "Lo siento, ha ocurrido un error al procesar tu mensaje.",
                'timestamp': None,
                'conversation_id': None
            })

    def process_message(self, message):
        try:
            message = message.lower()
            
            # Verificar si es un saludo
            if any(word in message for word in ['hola', 'hey', 'buenos días', 'buenas']):
                return random.choice(self.responses['respuestas_generales']['saludo'])

            # Verificar disponibilidad
            if any(word in message for word in self.responses['palabras_clave']['disponible']):
                return random.choice(self.responses['respuestas_generales']['inventario'])

            # Buscar por marca
            for marca in self.responses['palabras_clave']['marca']:
                if marca in message:
                    productos = []
                    # Buscar en laptops
                    productos.extend([p for p in self.responses['productos']['computadoras']['laptop'] 
                                   if p['marca'].lower() == marca])
                    # Buscar en desktops
                    productos.extend([p for p in self.responses['productos']['computadoras']['desktop'] 
                                   if p['marca'].lower() == marca])
                    
                    if productos:
                        response = f"📱 Productos {marca.upper()} disponibles:\n\n"
                        for producto in productos:
                            response += f"• {producto['modelo']}\n"
                            response += f"  💰 Precio: ${producto['precio']}\n"
                            specs = producto['specs']
                            response += "  🔧 Specs:\n"
                            for key, value in specs.items():
                                response += f"    - {key}: {value}\n"
                            response += "\n"
                        return response

            # Verificar si pregunta por precios
            if any(word in message for word in self.responses['palabras_clave']['precio']):
                return random.choice(self.responses['respuestas_generales']['precio'])

            # Si no se encuentra ninguna palabra clave específica
            if any(word in message for word in self.responses['palabras_clave']['ayuda']):
                return ("Puedo ayudarte con:\n"
                       "• Información sobre laptops y computadoras 💻\n"
                       "• Precios y especificaciones 💰\n"
                       "• Disponibilidad de productos 📦\n"
                       "• Recomendaciones según tus necesidades 🎯\n\n"
                       "¿Qué te gustaría saber?")

            return random.choice(self.responses['respuestas_generales']['no_entiendo'])
        except Exception as e:
            print(f"Error en process_message: {e}")
            return "Lo siento, ha ocurrido un error al procesar tu mensaje." 