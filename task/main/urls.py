from django.urls import path
from .views import item_view, ItemListView


urlpatterns = [
    path('item/<int:pk>', item_view, name='detail_item'),
    path('', ItemListView.as_view(), name='home')
]
