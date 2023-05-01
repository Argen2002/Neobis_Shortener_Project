from rest_framework import serializers

from  .models import Url

class UrlListSerializer(serializers.ModelSerializer):

    class Meta:
        model =Url
        fields = ('link')