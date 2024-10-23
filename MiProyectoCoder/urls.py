
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls import handler404
from fulanos.views import handler404

handler404 = handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/fulanos/', permanent=False)),  # Redirige la raíz a fulanos
    path('fulanos/', include('fulanos.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)