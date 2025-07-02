from django.urls import path
from TecnoClickApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('store/', views.tienda, name="Tienda"),

]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)