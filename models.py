from django.db import models


class Bikers_Choice(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image_url = models.CharField(max_length=2000)


    def __str__(self):
        return self.name




