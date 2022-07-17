# The Director class is a model that has a name field that is a CharField with a max length of 60.
from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=60, help_text="Ingresa el nombre del director")


    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=60, help_text="Titulo de la pelicula")
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    synopsis = models.CharField(max_length=120, help_text="Sinopsis de la pelicula")


    def __str__(self):
        return self.title