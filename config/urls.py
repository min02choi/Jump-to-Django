from django.contrib import admin
from django.urls import path, include

from pybo import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('/', include('pybo.urls')),
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('pybo/', include('pybo.urls')),
]
