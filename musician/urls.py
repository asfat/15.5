from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.musician,name='musician'),
    path('edit/<int:id>',views.musician_edit,name='musician_edit'),
]   