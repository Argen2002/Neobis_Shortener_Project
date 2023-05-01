# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from rest_framework import status
#
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Url
# from .serializers import UrlListSerializer
# import uuid
#
# def index(request):
#     return render(request, 'index.html')
#
#
# class UrlShortener(APIView):
#     def post(request):
#         link = request.data.get('url')
#         uid = str(uuid.uuid4())[:5]
#         new_url = Url(link=link, uuid=uid)
#         new_url.save()
#         return Response(uid)
#
#
# class Urllong(APIView):
#     def redirect_to_url(request, pk):
#         url_details = Url.objects.get(uuid=pk)
#         return redirect('https://' + url_details.link)
#
#
#
#
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
            # link = serializer.validated_data.get('link')
            # uid = str(uuid.uuid4())[:5]
            # # new_url = Url(link=link, uuid=uid)
            # new_url.save()
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Urllong(APIView):
    def get(self, request, pk, format=None):
        url_details = Url.objects.get(uuid=pk)
        return redirect(url_details.link)

