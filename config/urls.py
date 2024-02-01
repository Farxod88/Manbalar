"""
URL configuration for config project.

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from api.view.articles import ArticlesListViews
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_adminlte.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include('api.urls')),
    path('articles/', ArticlesListViews.as_view(), name='articles-list'),

]

               # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
