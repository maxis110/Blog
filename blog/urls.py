from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^register/$', views.registration, name='user_new'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.comments_add, name='comments_add'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comments_remove, name='comments_remove'),
    url(r'^(?P<pk>[0-9]+)/likes/$', views.add_likes, name='add_likes'),

]