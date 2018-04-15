from django.conf.urls import *
from django.views.generic import RedirectView
from django.urls import path, include

from django_messages.views import *

app_name = "messages"

urlpatterns = (
    path('', RedirectView.as_view(permanent=True, url='inbox/'), name='messages_redirect'),
    path('inbox/', inbox, name='messages_inbox'),
    path('outbox/', outbox, name='messages_outbox'),
    path('compose/', compose, name='messages_compose'),
    path('compose/<recipient>/', compose, name='messages_compose_to'),
    path('reply/(<message_id>/', reply, name='messages_reply'),
    path('view/(<message_id>/', view, name='messages_detail'),
    path('delete/(<message_id>)/', delete, name='messages_delete'),
    path('undelete/(<message_id>)/', undelete, name='messages_undelete'),
    path('trash/', trash, name='messages_trash'),
)
