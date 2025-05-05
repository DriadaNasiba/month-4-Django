from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from first_home_work.views import fist_home_wokr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fist_home_wokr),
    
]

urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT)