from django.urls import path, re_path
from twitter.views import MyView, test_tweet_view, Account
urlpatterns = [
#    re_path(r'^(?P<code>[^/]+)/api/$', Api_View.as_view()),
    path("mine/", MyView.as_view(), name="my_view"),
    path("test/", test_tweet_view, name="test_publish"),
    #path('account/', Account, name = "account"),
]
