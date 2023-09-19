from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin1/', admin.site.urls),
    path('', views.login, name='login'),
]