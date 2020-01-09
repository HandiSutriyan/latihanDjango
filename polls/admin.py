from django.contrib import admin

# Register your models here.

#import tabel question

from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)
