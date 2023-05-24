from django.db import models


class UserModels(models.Model):
    user_name: str = models.CharField()
    age: int = models.IntegerField()
