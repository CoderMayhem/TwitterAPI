from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TweetSerializer
from twitter.models import Tweet

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm


# Create your views here.


def login_view(request):
    
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request,user)
        
        return redirect('/twitter/tweet')

    context  = {
        'form' : form,
    }
    return render(request, "login.html",context)

def register_view(request):
    
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password = password)
        login(request,new_user)
        
        return redirect('/twitter')

    context  = {
        'form' : form,
    }
    return render(request, "sign_up.html",context)

def logout_view(request):
    logout(request)
    return redirect('/twitter')

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