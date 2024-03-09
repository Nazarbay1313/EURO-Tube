from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

from myproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 👇 2. Add the app url on this
    path('', include('myapp.urls')),
    path('', include('users.urls')),
    path('api/', include('api.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
