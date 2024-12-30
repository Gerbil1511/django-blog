from . import views
from django.urls import path

# urlpatterns here is a list of URL patterns. Each URL pattern is a
# call to the path() function. The path() function takes two required 
# arguments: route and view


urlpatterns = [ 
    path('', views.PostList.as_view(), name='home'),
]