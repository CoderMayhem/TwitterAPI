from django.urls import path
from twitter.views import *

urlpatterns = [
    path('', login_view),
    path('register/', register_view),
    path('logout/', logout_view),
    path('tweet/', TweetCreateView.as_view()),
    path('tweet/<int:pk>', TweetAPIView.as_view()),
    path('all/', TweetListView.as_view()),
    path('delete/', delete_tweet)
]