from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Relationship)
