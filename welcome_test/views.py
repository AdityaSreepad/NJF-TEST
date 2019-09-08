from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#@api_view(['GET', 'POST'])
#def login(request):
#    if request.method =='POST':
#        return Response('Login successful',status=status.HTTP_201_CREATED)

class Login(APIView):
    def post(self, request, format=None):
        print(request.headers['Host'])
        print(request.headers['username'])
        print(request.headers['password'])

        if request.headers['username'] in ('Aditya','Sushanth'):
            return Response('Login successful, Welcome :'+request.headers['username'],status=status.HTTP_201_CREATED)
        else:
            return Response('Login Failed, Invalid user :'+request.headers['username'], status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        print(request.headers)
        return Response('get request not allowed',status=status.HTTP_400_BAD_REQUEST)
