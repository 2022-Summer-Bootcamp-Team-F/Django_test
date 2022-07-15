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
from example.models import Image, Image_URL
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from storagetest.settings import IMAGE_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
import boto3, uuid

# Create your views here.

class im_url(APIView):
    def post(self, request):
        files = request.FILES.getlist('files')
        host_id = request.GET.get('host_id')
        s3r = boto3.resource('s3', aws_access_key_id= AWS_ACCESS_KEY_ID, aws_secret_access_key= AWS_SECRET_ACCESS_KEY)
        key = "%s" %(host_id)

        for file in files :
            file._set_name(str(uuid.uuid4()))
            s3r.Bucket(AWS_STORAGE_BUCKET_NAME).put_object( Key=key+'/%s'%(file), Body=file, ContentType='jpg')
            Image_URL.objects.create(
                image_url = IMAGE_URL+"%s/%s"%(host_id, file),
                host_id = host_id
            )
        return Response({'message' : 'done'})