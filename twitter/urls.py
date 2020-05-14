from django.urls import path
from twitter.views import *

urlpatterns = [
    path('', TweetCreateView.as_view()),
    path('<int:pk>', TweetAPIView.as_view()),
    path('all', TweetListView.as_view()),
    path('delete/<int:pk>', delete_tweet)
]