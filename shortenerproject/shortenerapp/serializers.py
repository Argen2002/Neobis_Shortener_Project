from rest_framework import serializers

import uuid

from .models import Url

#создания нового экземпляра модели Url
class UrlListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('link', 'uuid',)
        read_only_fields = ('uuid',)

    def create(self, validated_data):
        link = validated_data['link'] #проверенные данные значения link
        uid = str(uuid.uuid4())[:6] #генерация случачайной   с 6 символами с модулью uuid
        new_url = Url(link=link, uuid=uid)#создаем новый экземпляр модели Url, используя извлеченное значение link и сгенерированное значение uid
        new_url.save()
        return new_url



