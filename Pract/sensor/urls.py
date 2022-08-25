from django.contrib import admin
from django.urls import path
from sensor import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path ('', views.index,name= 'sensor'),
    path ('About', views.about,name= 'about'),
    path ('Services', views.services,name= 'services'),
    path ('Contact', views.contact,name= 'Contact'),
]
