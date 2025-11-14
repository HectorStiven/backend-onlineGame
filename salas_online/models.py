from django.db import models

# Create your models here.
class T001Salas(models.Model):
    t001_codigo = models.CharField(max_length=10, unique=True)  # Código de unión
    t001_creado = models.DateTimeField(auto_now_add=True)       # Fecha de creación

    class Meta:
        db_table = "T001_salas"