# Create your views here.
from testAPI.models import CaffeModel
from testAPI.serializers import CaffeModelSerializer

from rest_framework import viewsets


# Create your views here.
class CaffeModelViewSet(viewsets.ModelViewSet):
    queryset = CaffeModel.objects.all()
    serializer_class = CaffeModelSerializer