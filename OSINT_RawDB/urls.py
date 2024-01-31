"""
URL configuration for OSINT_RawDB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import main_db.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/add_articles', main_db.views.add_articles),
    path('api/get_articles', main_db.views.get_articles),
    path('api/delete_article/<int:article_id>', main_db.views.delete_article),
    path('api/update_article/<int:article_id>', main_db.views.update_article),
    path('api/update_word_cloud/<int:article_id>', main_db.views.update_word_cloud),
    path('api/get_word_cloud/<int:article_id>', main_db.views.get_word_cloud),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
