from rest_framework import serializers
import datetime


class SafeRoutesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=5000)
    location = serializers.CharField(max_length=255)
    lng = serializers.IntegerField()
    lat = serializers.IntegerField()
    userId = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    isdeleted = serializers.BooleanField()
    profilePicture = serializers.CharField(max_length=5000)
    videoUrl = serializers.CharField(max_length=255,default=None)
    images = serializers.CharField(max_length=255,default=None)
    mediatype = serializers.IntegerField()
    imagePaths = serializers.CharField(max_length=255,default=None)
    feedsComment = serializers.CharField(max_length=255,default=None)
    commentCount = serializers.IntegerField()

    def __str__(self):
        return dict(
            response = 200,
            message = 'Passed',
            time = datetime.datetime.now()
        )