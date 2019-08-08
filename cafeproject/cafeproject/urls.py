"""cafeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import mainpage.views
import startpage.views
import postapp.views
import accounts2.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainpage/', mainpage.views.main, name="main"),
    path('', startpage.views.start, name="start"),
    path('searchapp', include('searchapp.urls')),
    path('post/', postapp.views.post, name="post"),
    path('post/<int:post_id>/', postapp.views.detail, name="detail"),
    path('post/write/', postapp.views.write, name="write"),
    path('post/create/', postapp.views.create, name='create'),
    path('post/comment/<int:post_id>', postapp.views.comment, name="comment"),

    path('accounts2/', include('accounts2.urls')),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
