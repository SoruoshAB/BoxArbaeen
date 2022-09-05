from django.db import models


class Map(models.Model):
    fa_name = models.CharField(max_length=100)
    image = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.fa_name
