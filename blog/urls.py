from django.urls import path
from . import views
from .feeds import LatestPostFeeds


app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post-list-by-tag'),
    # path('', views.PostListView.as_view(), name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:postx>/',
         views.post_detail,
         name='post-detail'),
    path('<int:post_id>/share/', views.post_share, name='post-share'),
    path('<int:post_id>/comment/', views.post_comment, name='post-comment'),
    path('feed/', LatestPostFeeds(), name='post-feed'),
]
