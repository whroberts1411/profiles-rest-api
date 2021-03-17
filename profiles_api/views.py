
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

#------------------------------------------------------------------------------
class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializer

    #--------------------------------------------------------------------------
    def get(self, request, format=None):
        """ Returns a list of something """

        an_apiview = [
            'Get up at about 5:30 am',
            'Walk the dog for an hour or two',
            'Have a shower and get dressed again',
            'Have my breakfast and a large cup of coffee',
            'Switch on the computer and start work'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    #--------------------------------------------------------------------------
    def post(self, request):
        """ Create a message with our name """

        serializer = self.serializer_class(data=request.data)
        print('serializer :',serializer)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #--------------------------------------------------------------------------
    def put(self, request, pk=None):
        """ This will replace all of the requested object """

        return Response({'method':'PUT'})

    #--------------------------------------------------------------------------
    def patch(self, request, pk=None):
        """ This will replace part of the requested object """

        return Response({'method':'PATCH'})

    #--------------------------------------------------------------------------
    def delete(self, request, pk=None):
        """ This will delete the requested object """

        return Response({'method':'DELETE'})

#------------------------------------------------------------------------------
class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewset """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a message and list """

        a_viewset = [
            'Reading books about anything',
            'Taking photographs of landscapes and stuff',
            'Learning new programming skills',
            'Walking up and down mountains'
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})

    #--------------------------------------------------------------------------
    def create(self, request):
        """ Create a new object """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}, from my API'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #--------------------------------------------------------------------------
    def retrieve(self, request, pk=None):
        """ Get an object by its ID """

        return Response({'http_method':'GET'})

    #--------------------------------------------------------------------------
    def update(self, request, pk=None):
        """ Replace an object with new version """

        return Response({'http_method':'PUT'})

    #--------------------------------------------------------------------------
    def partial_update(self, request, pk=None):
        """ Update part of an object """

        return Response({'http_method':'PATCH'})

    #------------------------------------------------------------------------------
    def destroy(self, request, pk=None):
        """ Delete an object """

        return Response({'http_method':'DELETE'})

#------------------------------------------------------------------------------
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating, updating and deleteing user profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

#------------------------------------------------------------------------------
class UserLoginApiView(ObtainAuthToken):
    """ Create User Authentication Tokens """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

#------------------------------------------------------------------------------
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ For creating, reading and updating profile feed items """

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """ Set user profiles to the logged in user """
        serializer.save(user_profile=self.request.user)

#------------------------------------------------------------------------------