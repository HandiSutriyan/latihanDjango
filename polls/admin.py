from django.contrib import admin

# Register your models here.

#import tabel question

from .models import Question

admin.site.register(Question)
