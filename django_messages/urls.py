from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django_messages.views import *

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': "django_messages/index.html"}, name='messages'),
    url(r'^inbox/$', inbox, name='messages_inbox'),
    url(r'^outbox/$', outbox, name='messages_outbox'),
    url(r'^compose/$', compose, name='messages_compose'),
    url(r'^compose/(?P<recipient>[\w.@+-]+)/$', compose, name='messages_compose_to'),
    url(r'^reply/(?P<message_id>[\d]+)/$', reply, name='messages_reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', view, name='messages_detail'),
    url(r'^mark_as_read/(?P<message_id>[\d]+)/$', mark_as_read, name='messages_mark_as_read'),
    url(r'^delete/(?P<message_id>[\d]+)/$', delete, name='messages_delete'),
    url(r'^undelete/(?P<message_id>[\d]+)/$', undelete, name='messages_undelete'),
    url(r'^trash/$', trash, name='messages_trash'),
)
