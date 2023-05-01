from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Url
from .serializers import UrlListSerializer


class UrlShortener(APIView):#Класс UrlShortener наследуется от APIView и имеет метод post, который принимает запрос
    def post(self, request):
        serializer = UrlListSerializer(data=request.data)
        if serializer.is_valid():# проверки валидности и сохраняются в базе данных
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)#ответ в формате JSON с данными и статусом HTTP 201 CREATED в случае успешного создания объекта
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Urllong(APIView):#наследуется от APIView и имеет метод get, который принимает запрос
    def get(self, request, pk, format=None):
        url_details = Url.objects.get(uuid=pk)
        return redirect(url_details.link) #извлекает данные из базы данных и перенаправляет на длинную ссылку (url_details.link) с помощью функции redirect().

