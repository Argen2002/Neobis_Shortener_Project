from django.urls import path
from . import views
from .views import (
    #index,
    UrlShortener,
    Urllong,

)

urlpatterns = [
    #path('', index, name='index'),
    path('shorten/', UrlShortener.as_view()),
    path('shorten/<str:pk>/', Urllong.as_view(), name='redirect_to_url'),

]
