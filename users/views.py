from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, UserSerializer
from rest_framework.response import Response

# User Registration
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# User Profile: retrieve and update
class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user