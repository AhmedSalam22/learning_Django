from django.contrib import admin
from .models import Category , States , Site  ,Iso , Region 
# Register your models here.
admin.site.register([Category , States , Site  ,Iso , Region ])