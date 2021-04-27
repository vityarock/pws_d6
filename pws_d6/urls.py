from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls', namespace="p_library")),
    path('', views.index),
    path('index/', views.index),
    path('publishers/', views.pub_list),
    path('readers/', views.reader_list),
]
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
