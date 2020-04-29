from django.contrib import admin
from review.models import *

class ReviewAdmin(admin.ModelAdmin):
    reviews_display = ('review_text', 'username', 'tea')
    # teas_display = ('tea_name')

# Register your models here.
# admin.site.register(Tea)
admin.site.register(Review)
admin.site.register(UserProfileInfo)
