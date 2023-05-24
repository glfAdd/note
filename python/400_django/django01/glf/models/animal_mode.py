from django.db import models


class AnimalModel(models.Model):
    animal_name = models.CharField()
    status = models.IntegerField()

    class Meta:
        db_table = 'model'
