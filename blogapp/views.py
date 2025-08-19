from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blogapp.serializers import UserRegistrationSerializer


# Create your views here.
@api_view(["POST"])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
