from django.contrib import admin

from .models import djangoClasses, Biology, History, Calculus


# Register your models here.
admin.site.register(djangoClasses)
admin.site.register(Biology)
admin.site.register(History)
admin.site.register(Calculus)
