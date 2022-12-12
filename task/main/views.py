from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ListSerializer


class ItemListView(generics.ListAPIView):
    """All Items objects with filters"""
    queryset = Item.objects.all()
    serializer_class = ListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['article', 'name', 'status']


@api_view(['GET'])
def item_view(request, pk):
    """ItemDetail"""
    queryset = Item.objects.filter(pk=pk)
    serializer = ListSerializer(queryset, many=True)
    return Response(serializer.data)
