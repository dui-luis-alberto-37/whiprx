from django.urls import path, re_path
from twitter.views import MyView

urlpatterns = [
#    re_path(r'^(?P<code>[^/]+)/api/$', Api_View.as_view()),
    path("mine/", MyView.as_view(), name="my-view"),
]
