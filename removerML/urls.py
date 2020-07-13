from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("upload", views.data, name="data")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
