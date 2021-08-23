from django.db import models

class djangoClasses (models.Model):
    title = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=30, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=3)


    objects = models.Manager()

    def __str__(self):
        return self.name
