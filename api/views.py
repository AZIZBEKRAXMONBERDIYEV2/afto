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





def get_product(request: Response) -> Request:
            products = Aftosalon.objects.filter(model='Oppo')
            data = []
            for product in products:
                data.append(product.to_dict())
            return Response(data, safe=False)



class TaskList(APIView):



    def post(self , reqeust :  Request):
            
              # data=json.loads(d)
              # print(reqeust.data)
              serializer = TaskSerializer(data=reqeust.data)
              if serializer.is_valid():
                serializer.save()

                return Response({'save': 'ok'})
    



    def delete(self , request : Request ,   pk):
        
        Aftosalon.objects.filter(id=pk).delete()
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
    

    
    def get(self,request:Response,model=None , brent=None , rang=None , pk=None , yil=None , narx=None , min_narx=None,max_narx=None  ) ->Request:
            if model:
                    product = Aftosalon.objects.filter(model__contains = model)
                    data = []
                    for i in product:
                        data.append(i.to_dict())
                        
                    
                    return Response( data=data)
            
            elif brent:
                    product = Aftosalon.objects.filter(brent = brent)
                    data = []
                    for i in product:               
                        data.append(i.to_dict())
                    return Response(data=data)
            

            elif rang:
                    product = Aftosalon.objects.filter(rang = rang)
                    data = []
                    for i in product:               
                        data.append(i.to_dict())
                    return Response(data=data)
            

            elif pk:
                    product = Aftosalon.objects.filter(id = pk)
                    data = []
                    for i in product:               
                        data.append(i.to_dict())
                    return Response(data=data)
            

            elif yil:
                    product = Aftosalon.objects.filter(yil = yil)
                    data = []
                    for i in product:               
                        data.append(i.to_dict())
                    return Response(data=data)
            

            elif narx:
                    product = Aftosalon.objects.filter(narx = narx)
                    data = []
                    for i in product:               
                        data.append(i.to_dict())
                    return Response(data=data)
            

            elif min_narx and max_narx:
                products = Aftosalon.objects.filter(narx__gte=min_narx, narx__lte=max_narx)
            elif min_narx:
                products = Aftosalon.objects.filter(narx__gte=min_narx)
            elif max_narx:
                products = Aftosalon.objects.filter(narx__lte=max_narx)

                data = []
                for product in products:
                    data.append(product.to_dict())

                return Response(data=data)
                
            else:
                product = Aftosalon.objects.all()
                data = []
                for i in product:
                        data.append(i.to_dict())
                return Response({"data":data})