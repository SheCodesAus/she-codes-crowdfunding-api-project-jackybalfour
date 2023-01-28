from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CustomUser
from .serializers import CustumUserSerializer


class CustomUserList(APIView):

    def get(self,request):
        users= CustomUser.objects.all()
        serializer = CustumUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustumUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CustomUserDetail(APIView):

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self, resquest, pk):
        user = self.get_object(pk)
        serializer = CustumUserSerializer(user)
        return Response(serializer.data)
