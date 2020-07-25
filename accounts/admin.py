from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Role)
admin.site.register(Blogger)
admin.site.register(Post)
admin.site.register(Comment)