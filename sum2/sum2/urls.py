
from django.contrib import admin
from django.urls import path,include
from.import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('child_app.urls')),
    path('about/',include('about.urls')),
    path('client/',include('client.urls')),
    path('portfulio/',include('portfulio.urls')),
    path('home/',include('home.urls')),
    path('survice/',include('survice.urls')),
    path('contact/',include('contact.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
