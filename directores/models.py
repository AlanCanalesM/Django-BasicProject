from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=60, help_text="Ingresa el nombre del director")


    def __str__(self):
        return self.name
