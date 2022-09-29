from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Media
from .serializers import MediaServiceSerializer


class MediaServiceView(ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaServiceSerializer

    def perform_create(self, serializer):
        s_id = self.request.data['service_id']
        last_obj = Media.objects.filter(service_id=s_id).last()

        if last_obj != None:
            last_obj = Media.objects.filter(service_id=s_id).latest('created_at')
            last_obj.delete()

        serializer.save()


class DetailMediaServiceView(RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaServiceSerializer