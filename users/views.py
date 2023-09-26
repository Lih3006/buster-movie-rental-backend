from django.shortcuts import get_object_or_404
from rest_framework.views import status, Request, Response, APIView
from .models import User
from .serializers import CustomJWTSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsUserLoged


class UserView(APIView):    
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data
        find_username = User.objects.filter(username=user_data['username']).first()
        find_email = User.objects.filter(email=user_data['email']).first()
            
        error_response = {}
        
        if find_email:
            error_response['email'] = ['email already registered.']
        if find_username:
            error_response['username'] = ['username already taken.']
        if error_response:
            return Response(error_response, status.HTTP_400_BAD_REQUEST)
                
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)
    

class UserDetailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserLoged]
    
    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def patch(self, request: Request, user_id: int) -> Response:
        user_obj = User.objects.get(id=user_id)
        self.check_object_permissions(request, user_obj)
        serializer = UserSerializer(user_obj, request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
        

class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
    