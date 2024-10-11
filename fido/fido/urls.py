# main urls.py
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('token_authentication.urls')),  # replace with your auth app name
    path('users/', include('users.urls')),  # replace with your user app name
]
