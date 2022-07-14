# from urllib import response
# from django.http import HttpResponse
from django.shortcuts import render
from example import serializers
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
from example.serializers import ImSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from example.models import Image
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

# Create your views here.

class im_list(APIView):
    def get(self, request):
        data = Image.objects.all()
        serializer = ImSerializer(data, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'done'})
        
        return Response(serializer.errors)

class im_detail(APIView):
    def get_object(self,pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Http404
    
    def get(self, request, pk):
        data = self.get_object(pk)
        serializer = ImSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk):
        im = self.get_object(pk)
        serializer = ImSerializer(im, data=request.data)
        if serializer.is_valid():
            serializer.saver()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
              
# @csrf_exempt
# def im_list(request):
#     if request.method == 'GET':
#         query_set = Image.objects.all()
#         serializer = ImSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request, media_type=Any)
#         serializer = ImSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
    
#     return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def im_detail(request, pk):
#     obj = Image.objects.get(id=pk)

#     if request.method == 'GET':
#         serializer = ImSerializer(obj)
#         return JsonResponse(serializer.data, safe = False)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ImSerializer(obj, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         obj.usage_fg = 'N'
#         obj.save()
#         return HttpResponse(status=204)