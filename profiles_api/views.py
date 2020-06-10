from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

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


    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                    serializer.errors,
                    status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ To update an object"""
        return Response({'message':'PUT'})

    def patch(self, request, pk=None):
        return({'message':'Patch'})

    def delete(self,request,pk=None):
        return Response({'message':'Delete'})
