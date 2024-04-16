from django.contrib import admin
from django.urls import path, include
from bookstore.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls'))
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

