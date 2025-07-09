from rest_framework import serializers
from internationalSwelfare.models import Hostel
from internationalSwelfare.models import Admin,Student
from django.contrib.auth.models import User
class HostelSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Hostel
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['admin_id', 'user', 'phone', 'created_at']    
  


class StudentRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    nationality = serializers.CharField()
    passport_number = serializers.CharField()
    university = serializers.CharField()
    year_of_study = serializers.IntegerField()
    course = serializers.CharField()
    admission_number = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['admission_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        Student.objects.create(
            user=user,
            nationality=validated_data['nationality'],
            university=validated_data['university'],
            phone_number=validated_data['phone_number'],
        )
        return user
