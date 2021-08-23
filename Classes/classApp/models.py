from django.db import models

class djangoClasses (models.Model):
    title = models.CharField(max_length=30)
    number = models.IntegerField(max_length=10)
    name = models.CharField(max_length=30, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=3)


    objects = models.Manager()

    def __str__(self):
        return self.name


#objects of class "djangoClasses"
Biology = djangoClasses(title="Biology", number=101, name="Bill Cyrus", duration=1.5)
Biology.save()

History = djangoClasses(title="History", number=100, name="Lily Sue", duration=1)
History.save()

Calculus = djangoClasses(title="Calculus", number=200, name="Stephanie Gaby", duration=2.5)
Calculus.save()
