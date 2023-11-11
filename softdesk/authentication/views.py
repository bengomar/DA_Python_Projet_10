from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import User
from .permissions import CreateUserAllowedOrReadOnly
from .serializers import UserSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CreateUserAllowedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Gets the serializer
        serializer.is_valid(raise_exception=True)  # Checks if the data is valid
        age = serializer.validated_data.get("age")
        if age is not None and int(age) < 15:
            return Response(
                {"error": "Inscription interdite aux moins de 15 ans"},
            )
        user = User(username=serializer.validated_data.get("username"), age=age)
        user.set_password(
            serializer.validated_data.get("password")
        )  # Sets the password correctly
        user.save()
        return Response(UserSerializer(user).data)
