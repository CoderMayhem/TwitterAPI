from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TweetSerializer
from twitter.models import Tweet



# Create your views here.

def delete_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    tweet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class TweetCreateView(APIView):
    
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TweetAPIView(APIView):

    def get(self, request, pk):
        tweet = get_object_or_404(Tweet, pk=pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)



class TweetListView(APIView):
    
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many = True)
        return Response(serializer.data)