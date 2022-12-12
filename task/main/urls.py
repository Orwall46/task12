from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import item_view, ItemListView


urlpatterns = [
    path('item/<int:pk>', item_view, name='detail_item'),
    path('', ItemListView.as_view(), name='home')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
