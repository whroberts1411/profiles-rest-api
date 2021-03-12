from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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