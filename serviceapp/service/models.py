from django.db import models

class Service(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    type_service = models.CharField(max_length=150)
    numero = models.Field()
    tarifs = models.FloatField(default=0)

    def __str__(self):
        return self.nom
