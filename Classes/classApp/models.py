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
Class1 = djangoClasses('Biology', 101, 'Bill Cyrus', 1.5)
Class2 = djangoClasses('History', 100, 'Lilly Covfefe', 1)
Class3 = djangoClasses('Calculus', 110, 'Stephanie Gaby', 120)
