from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Url
from .serializers import UrlListSerializer


class UrlShortener(APIView):
    def post(self, request, format=None):
        serializer = UrlListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Urllong(APIView):
    def get(self, request, pk, format=None):
        url_details = Url.objects.get(uuid=pk)
        return redirect(url_details.link)

