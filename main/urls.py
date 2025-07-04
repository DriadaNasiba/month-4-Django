from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_home_work.urls')),     
    path('films/', include('films.urls')),          
    path('tags/', include('tags.urls')),            
    path('parser/', include('parser_app.urls')),    
    path('users/', include('users.urls')),   
    path('food/', include('food.urls')),
       
]


urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                    document_root=settings.STATIC_ROOT)