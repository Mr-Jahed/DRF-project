from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome! Go to /api/external/ or /api/create/")

urlpatterns = [
    path('', home),  # 👈 root path
    path('admin/', admin.site.urls),
    path('api/', include('demo.urls')),
]
