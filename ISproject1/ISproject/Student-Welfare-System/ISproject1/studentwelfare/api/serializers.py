from rest_framework import serializers
from internationalSwelfare.models import Hostel
from internationalSwelfare.models import Admin
class HostelSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Hostel
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['admin_id', 'user', 'phone', 'created_at']        