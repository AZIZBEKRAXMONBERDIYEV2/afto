from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

import json
from django.contrib.auth.models import User
from .models import Aftosalon

from .serializers import TaskSerializer, UserSerializer



class TaskList(APIView):



    def post(self , reqeust :  Request):
            
              # data=json.loads(d)
              # print(reqeust.data)
              serializer = TaskSerializer(data=reqeust.data)
              if serializer.is_valid():
                serializer.save()

                return Response({'save': 'ok'})
    



    def delete(self , request : Request ,   pk):
        
        data = Aftosalon.objects.filter(id=pk).delete()
        # print()
        return Response({"aftosalon_delete" : "oK"})
    

    def put(self , request : Request ,   pk):
      try:
          task = Aftosalon.objects.get(id=pk)
      except Aftosalon.DoesNotExist:
          return Response({"error": "Task not found"}, status=404)
      
      serializer = TaskSerializer(task, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=400)
    
    def get(self, request: Request, pk: int) -> Response:
        task = Aftosalon.objects.filter(id=pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
              