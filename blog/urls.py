from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view()),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^register/$', views.user_new, name='user_new'),

]