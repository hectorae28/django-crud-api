from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('api/',include(('projects.urls','projetcs'),namespace='projects')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token)
]
