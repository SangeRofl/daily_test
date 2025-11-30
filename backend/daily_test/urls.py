from django.contrib import admin
from django.urls import path, include
from articles.urls import articles_api_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(articles_api_router.urls)),

    path('articles/', include('articles.urls')),
]
