from rest_framework import serializers
from django.conf import settings


class ListSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        formats = obj.get_format()
        file_name = str(obj.image).replace('.webp', '')
        return {
            'id': obj.pk,
            'name': obj.name,
            'article': obj.article,
            'price': obj.price,
            'status': obj.status,
            'image': {
                'path': f'{settings.MEDIA_URL}{file_name}',
                'formats': formats
            }
        }
