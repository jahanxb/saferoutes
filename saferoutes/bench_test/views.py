from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
import json
from rest_framework import generics
# Create your views here.
from .serializer import SafeRoutesSerializer
import os

class SafeResponse(APIView):

    def get(self,request,format=None):
        f = open(os.path('/home/jahan/saferoutes/data.json'))
        #f = open('D://PycharmProjects/saferoutes/data.json',encoding='UTF-8')

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        return Response(data)



class PostResponse(APIView):
    def post(self,request):
        mdata = request.data
        ndata = mdata.get('feeds')

        #data.append(name)
        #name = data.get('name')
        return Response({
            "response": 200,
            "Message": "Passed",
            "data": ndata
        })


class ViewSafeResponse(generics.CreateAPIView):
    serializer_class = SafeRoutesSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            mdata = request.data
            ndata = mdata.get('feeds')
            #print(ndata)
            for item in ndata:
                id = item.get('id')
                print(id)
                title = item.get('title')
                description = item.get('description')
                location = item.get('location')
                lng = item.get('lng')
                lat = item.get('lat')
                userId = item.get('userId')
                name = item.get('name')
                isdeleted = item.get('isdeleted')
                profilePicture = item.get('profilePicture')
                videoUrl = item.get('videoUrl')
                images = item.get('images')
                mediatype = item.get('mediatype')
                imagePaths = item.get('imagePaths')
                feedsComment = item.get('feedsComment')
                commentCount = item.get('commentCount')
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({
                "response": 404,
                "Message": "Failed",
                "Exception": str(e)
            })


