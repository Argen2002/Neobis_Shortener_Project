from django.urls import path
from .views import (
    UrlShortener,
    Urllong,

)

urlpatterns = [
    path('shorten/', UrlShortener.as_view()),
    path('shorten/<str:pk>/', Urllong.as_view(), name='redirect_to_url'),

]
