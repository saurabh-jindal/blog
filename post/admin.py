from django.contrib import admin
from .models import Tag, Post
# Register your models here.
"""
Admin used for administrator
Username : sj
password : Heythere@
"""

admin.site.register((Tag, Post))
