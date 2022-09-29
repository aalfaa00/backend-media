from rest_framework import serializers
from .models import Media

class MediaServiceSerializer(serializers.ModelSerializer):
    service_id = serializers.CharField(max_length=10)

    class Meta:
        model = Media
        fields = ['id', 'file', 'created_at', 'service_id', 'service_type']
        read_only_fields = ['service_id', ]