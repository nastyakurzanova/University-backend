from django.contrib import admin
from .models import Book
from .models import Users
from .models import Audiences

admin.site.register(Audiences)
admin.site.register(Book)
admin.site.register(Users)
# Register your models here.
