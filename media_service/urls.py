from django.urls import path
from .views import MediaServiceView, DetailMediaServiceView

app_name = 'Media'

urlpatterns = [
    path('', MediaServiceView.as_view(), name='media-service'),
    path('<uuid:pk>', DetailMediaServiceView.as_view(), name='detail-media-service')
]