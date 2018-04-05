from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    url(r'^del_entry/(?P<entry_id>\d+)/$', views.del_entry, name='del_entry'),
    url(r'^api/topics/$', views.api_topics, name='api_topics'),
    # TODO:将api路径放到根url下,include相同内容，在views中判断并分别处理
]
