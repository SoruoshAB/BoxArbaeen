from django.db import models


class Video(models.Model):
    type_choices = [(1, "مستند"), (2, "کلیپ"), (3, "نماهنگ")]
    fa_name = models.CharField(max_length=250)
    image = models.TextField()
    link = models.TextField()
    type = models.IntegerField(choices=type_choices)

    def __str__(self):
        return self.fa_name
