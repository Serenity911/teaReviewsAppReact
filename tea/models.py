from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tea(models.Model):
    tea_name = models.CharField(max_length = 30)
    def __str__(self):
        return self.tea_name