from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from internationalSwelfare.models import Hostel
from internationalSwelfare.models import Admin, Student, EmergencyReport
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import HostelSerializer
from .serializers import AdminSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.views import APIView
@api_view(['GET'])
def getData(request):
    hostel = Hostel.objects.all() 
    serializer = HostelSerializer(hostel, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_admin(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        phone = request.data.get('phone')

        user = User.objects.create_user(username=username, password=password)
        admin = Admin.objects.create(user=user, phone=phone)
        serializer = AdminSerializer(admin)
        return Response({'message': 'Admin registered successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)




@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')

    user = authenticate(request, username=email, password=password)
    if user is not None:
        if role =='admkin':
            if not user.is_staff:
                return Response({'error': 'User is not an admin'}, status=status.HTTP_403_FORBIDDEN)
        return Response({
            'message': 'Login successful',
            'user_id': user.id,
            'role': role
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    



from django.contrib.auth.hashers import make_password

class RegisterStudentView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]  

    def post(self, request):
        data = request.data
        try:
            if User.objects.filter(username=data['admission_number']).exists():
                return Response({"error": "User already exists"}, status=400)

            user = User.objects.create(
                username=data['admission_number'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=make_password(data['password']),
            )

            Student.objects.create(
                user=user,
                nationality=data['nationality'],
                university=data['university'],
                phone_number=data['phone_number'],
            )

            return Response({"message": "Student registered successfully!"}, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class EmergencyReportView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            EmergencyReport.objects.create(
                user=request.user,
                type=data['type'],
                description=data['description'],
            )
            return Response({"message": "Emergency reported!"}, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=500)        
