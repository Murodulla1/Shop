from django.db import models

class Shop(models.Model):

    email = models.EmailField(max_length=250)
    number = models.BigIntegerField(default=0)  #narxi
    name = models.CharField(max_length=250, blank=False, null=False)
    familya = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.name