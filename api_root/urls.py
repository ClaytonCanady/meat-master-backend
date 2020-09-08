from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('meat_master_api.urls')),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls'))
]
