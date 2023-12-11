from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Questions)
admin.site.register(models.time)
admin.site.register(models.score)
admin.site.register(models.fraud_model)
