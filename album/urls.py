from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.album,name='album'),
    path('edit/<int:id>',views.album_edit,name='album_edit'),
    path('delete/<int:id>',views.delete_add,name='delete')
]   