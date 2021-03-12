from rest_framework.views import APIView
from rest_framework.response import Response

#------------------------------------------------------------------------------
class HelloApiView(APIView):
    """ Test API View """

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


#------------------------------------------------------------------------------