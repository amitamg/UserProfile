from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^api/cintauser$', user_list),
    url(r'^api/cintauser/(?P<pk>[0-9]+)$', user_detail),
]