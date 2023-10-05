from django.contrib import admin
from django.urls import path
from pythonproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetRoomSearch),
    path('order/<int:id>/', views.GetRoom, name='order_url'),
]