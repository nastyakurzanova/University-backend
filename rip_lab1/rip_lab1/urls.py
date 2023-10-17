from django.contrib import admin
from django.urls import path
from pythonproject import views
# from pythonproject import connect

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.GetRoomSearch),
    path('', views.bookList),
    path('book/<int:id>/', views.GetBook, name='book_url'),
    path('order/<int:id>/', views.GetRoom, name='order_url'),
]