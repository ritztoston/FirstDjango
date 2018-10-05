from django.urls import path
from register_user import views

urlpatterns = [
    path('', views.index, name='index'),
]
