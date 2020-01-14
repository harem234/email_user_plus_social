from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import status
from rest_framework.response import Response
from user_api.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class UpdateUserView(generics.UpdateAPIView):
    """update an existing user in the system"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]


class DeactivateUserView(generics.DestroyAPIView):
    """update an existing user in the system"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def delete(self, request, *args, **kwargs):
        # user = self.request.user
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_403_FORBIDDEN, data='user deactivated')


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    # obtain_auth_token view explicitly uses JSON requests and responses,
    # rather than using default renderer and parser classes in your settings, link below.
    # https://www.django-rest-framework.org/api-guide/authentication/#generating-tokens
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    # Authorization: Token <Token value>
    # authentication.SessionAuthentication
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user
