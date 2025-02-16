from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from products.models import Product

class ChatViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def send_message(self, request):
        user_message = request.data.get('message')
        conversation_id = request.data.get('conversation_id')
        
        # Crear o obtener conversación
        if conversation_id:
            conversation = Conversation.objects.get(id=conversation_id)
        else:
            conversation = Conversation.objects.create(user=request.user if request.user.is_authenticated else None)
        
        # Guardar mensaje del usuario
        Message.objects.create(
            conversation=conversation,
            is_user=True,
            content=user_message
        )
        
        # Procesar mensaje y generar respuesta
        response_content = self.process_message(user_message)
        
        # Guardar respuesta del bot
        bot_message = Message.objects.create(
            conversation=conversation,
            is_user=False,
            content=response_content
        )
        
        return Response({
            'conversation_id': conversation.id,
            'response': response_content,
            'timestamp': bot_message.timestamp
        })
    
    def process_message(self, message):
        """
        Procesa el mensaje del usuario y genera una respuesta
        Aquí implementarías la lógica del chatbot
        """
        # Ejemplo simple de respuesta basada en palabras clave
        message = message.lower()
        
        if 'computadora' in message or 'laptop' in message:
            laptops = Product.objects.filter(category='LAPTOP')
            if laptops.exists():
                response = f"Tenemos {laptops.count()} computadoras disponibles:\n"
                for laptop in laptops:
                    response += f"- {laptop.brand} {laptop.name}: ${laptop.price}\n"
            else:
                response = "Lo siento, actualmente no tenemos computadoras en stock."
                
        elif 'precio' in message:
            response = "Por favor, especifica qué producto te interesa y te diré su precio."
            
        else:
            response = "¿En qué puedo ayudarte? Puedo informarte sobre nuestros productos, precios y disponibilidad."
            
        return response 