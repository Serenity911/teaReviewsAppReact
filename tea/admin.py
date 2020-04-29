from django.contrib import admin
from tea.models import *

class ReviewAdmin(admin.ModelAdmin):
    teas_display = ('tea_name')

# Register your models here.
admin.site.register(Tea)
# admin.site.register(Review)