from django.urls import path

from blog.views import HomeView
from blog.views import PostView

urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
    path('', HomeView.as_view(), name='home'),
]