from django.shortcuts import render
from ehlfk.serializers import UrlSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ehlfk.models import Image_URL
from rest_framework.views import APIView
from django.http import Http404
from ektl.settings import IMAGE_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
import boto3, uuid
from django.views.generic import ListView


# Create your views here.

class im_url(APIView):
    def post(self, request):
        files = request.FILES.get('files')
        s3r = boto3.resource('s3', 
        aws_access_key_id= AWS_ACCESS_KEY_ID, 
        aws_secret_access_key= AWS_SECRET_ACCESS_KEY)

        files._set_name(str(uuid.uuid4()))
        s3r.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key='image/%s'%(files), 
            Body=files, 
            ContentType='jpg')
        Image_URL.objects.create(
            image_url = IMAGE_URL + 'image/' + "%s"%(files),
            )
        return Response({'message' : 'done'})

    def get(self,request):
        data = Image_URL.objects.all()
        serializer = UrlSerializer(data, many=True)
        return Response(serializer.data)
    
class im_detail(APIView):
    def get_object(self,pk):
        try:
            return Image_URL.objects.get(pk=pk)
        except Image_URL.DoesNotExist:
            return Http404
    
    # def get(self, request, image_id):
    #     data = self.get_object(image_id)
    #     serializer = UrlSerializer(data)
    #     return Response(data.image_url)
    
    def get(self, request, image_id):
        data = Image_URL.objects.get(image_id=image_id)
        serializer = UrlSerializer(data)
        return Response(serializer.data)


        #return Response({Image_URL.image_url})
#    return Response(serializer.errors)
class HomePageView(ListView):
    model = Image_URL
    template_name = "home.html"
    