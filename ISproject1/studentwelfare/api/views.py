from rest_framework.response import Response
from rest_framework.decorators import api_view
from internationalSwelfare.models import Hostel
from .serializers import HostelSerializer

@api_view(['GET'])
def getData(request):
    hostel = Hostel.objects.all() 
    serializer = HostelSerializer(hostel, many=True)
    return Response(serializer.data)