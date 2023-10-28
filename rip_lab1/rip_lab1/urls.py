from django.contrib import admin
from django.urls import path
from pythonproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetRoomSearch, name="all_cargo"),
    path('order/<int:id>/', views.GetRoom, name='order_url'),
    path('deleteCargo/', views.DeleteCurrentCargo, name = 'del_room_cargo')
   # path('', views.bookList),
    # path('book/<int:id>/', views.GetBook, name='book_url')
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)