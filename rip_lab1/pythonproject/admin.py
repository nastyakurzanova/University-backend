from django.contrib import admin
from .models import Book
from .models import Users
from .models import Audiences
from .models import Booking_requests

admin.site.register(Audiences)
admin.site.register(Book)
admin.site.register(Users)
admin.site.register(Booking_requests)
