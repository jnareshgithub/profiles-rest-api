from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self,request,format=None):
        """ Return a list of API features"""
        an_apiview = [  'narsh kumar',
                        'LogicSpear',
                        'SecurityMiddleware',
                        'Maintenence',
                        564569874,
                        223641232,
        ]

        return Response({'message':'Thanks for cosulting LogicSpear...','our_info':an_apiview})
