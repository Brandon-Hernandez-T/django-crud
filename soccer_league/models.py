from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    age_range = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    # Otros campos como posición, estatura, etc.

    def __str__(self):
        return self.name
    
