from django.db import models
from django.contrib.auth.models import User
# from tea.models import *
import tea.models


class Review(models.Model):
    review_text = models.CharField(max_length = 100)
    username = models.CharField(max_length = 15)
    tea = models.ForeignKey(tea.models.Tea, on_delete = models.CASCADE)
    def __str__(self):
        return self.review_text

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    def __str__(self):
        return self.user.username