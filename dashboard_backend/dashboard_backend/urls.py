#dashboard_backend\urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('data_api.urls')),  # Aqui inclui o arquivo 'urls.py' do app data_api
]
