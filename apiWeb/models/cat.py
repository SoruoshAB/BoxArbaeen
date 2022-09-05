from django.db import models


class Category(models.Model):
    category_id = models.PositiveIntegerField(primary_key=True, unique=True)
    icon_link = models.TextField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
