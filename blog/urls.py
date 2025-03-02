from django.urls import path # type: ignore

from . import views

from .feeds import LatestPostsFeed # type: ignore

app_name = 'blog'

urlpatterns = [
    # post views

    # path('post/list.html', views.post_list, name='post_list'),
    #path('', views.post_list, name='post_list'),
    #path('', views.PostListView.as_view(), name='post_list'),
    #path('<int:id>/', views.post_detail, name='post_detail'),

    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/', 
        views.post_detail, 
        name='post_detail'
    ),      
    path('', views.home_page, name='home_page'),   
    #path('home.html', views.home_page, name='home_page'),
    #path('post/home.html', views.home_page, name='home_page'),

    path(
        'tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'
    ),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path(
        'comment/<int:post_id>/comment/', views.post_commented, name='post_commented'
    ),

    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('comment/<int:post_id>/comment_page/', views.comment_page, name='comment_page'),

    path('comment/<int:comment_id>/edit_comment/', views.edit_comment, name='edit_comment'),
]
