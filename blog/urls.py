from django.urls import path
from . import views

# urlpatterns here is a list of URL patterns. Each URL pattern is a
# call to the path() function. The path() function takes two required
# arguments: route and view


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
