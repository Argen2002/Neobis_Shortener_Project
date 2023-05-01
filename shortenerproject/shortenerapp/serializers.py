import uuid
from rest_framework import serializers

from .models import Url


class UrlListSerializer(serializers.ModelSerializer):
    #link=serializers.URLField(write_only=True)
    class Meta:
        model = Url
        fields = ('link', 'uuid',)
        read_only_fields = ('uuid',)

    def create(self, validated_data):
        link = validated_data['link']
        uid = str(uuid.uuid4())[:6]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return new_url



