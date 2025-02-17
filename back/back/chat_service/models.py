from django.db import models
from django.contrib.auth.models import User
from django.db import models
class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    started_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id} - {self.started_at}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    is_user = models.BooleanField(default=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

class ChatResponse(models.Model):
    category = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.keyword}"

class productos(models.Model):
    categoria = models.TextField()
    tipo = models.TextField()
    marca = models.TextField()
    modelo = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    specs = models.JSONField()
    class Meta:
        db_table = 'productos'

    def __str__(self):
        return f"{self.categoria} - {self.tipo} - {self.marca} - {self.modelo}"

class respuestas_generales(models.Model):
    tipo = models.TextField()
    respuesta = models.TextField()

    class Meta:
        db_table = 'respuestas_generales'

    def __str__(self):
        return f"{self.tipo} - {self.respuesta}"

class PalabrasClave(models.Model):
    categoria = models.TextField()
    palabras = models.JSONField()

    class Meta:
        db_table = 'palabras_clave'

    def __str__(self):
        return f"{self.categoria} - {self.palabras}"


