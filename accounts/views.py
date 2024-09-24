# # accounts/views.py

# from rest_framework import generics, status
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from .models import User, RoleMaster
# from .serializers import UserSerializer, UserLoginSerializer

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

# # accounts/views.py

# from rest_framework.authtoken.models import Token

# class LoginView(generics.GenericAPIView):
#     serializer_class = UserLoginSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         email = serializer.validated_data['email']
#         password = serializer.validated_data['password']

#         try:
#             user = User.objects.get(email=email)
#             if user.check_password(password):
#                 # Generate or get the token
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'message': 'Login successful', 'token': token.key}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         except User.DoesNotExist:
#             return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)


# accounts/views.py

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User, RoleMaster
from .serializers import UserSerializer, UserLoginSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                # Return a response with user info or token
                return Response({'message': 'Login successful', 'user': user.email}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
