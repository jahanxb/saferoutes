from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [

    path('',views.SafeResponse.as_view()),
    path('post_test/',views.ViewSafeResponse.as_view()),
    path('post/',views.PostResponse.as_view())
]