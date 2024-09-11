from django.db import models
from Apps.Catalogos.Persona.models import Persona

# Create your models here.
class Cliente(models.Model):
    Cedula = models.CharField(max_length = 16)
    PersonId = models.ForeignKey(Persona, on_delete = models.RESTRICT)

    class Meta:
        db_table = 'Cliente'

    def __str__(self):
        return self.Cedula