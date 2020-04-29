from django.db import models
from django.contrib.auth.models import User


class Tea(models.Model):
    tea_name = models.CharField(max_length = 30)
    def __str__(self):
        return self.tea_name

class Review(models.Model):
    review_text = models.CharField(max_length = 100)
    username = models.CharField(max_length = 15)
    tea = models.ForeignKey(Tea, on_delete = models.CASCADE)
    def __str__(self):
        return self.review_text

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    def __str__(self):
        return self.user.username