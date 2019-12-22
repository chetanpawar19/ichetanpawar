from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import home.views
from notes import views

urlpatterns = [
    path('', home.views.home, name='index'),
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
