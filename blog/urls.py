from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # The first slug is call path converter while the second is a keyword name. 
    # The slug keyword name matches the slug parameter in the get method of the 
    # PostDetails class in the blog/view.py file.
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]