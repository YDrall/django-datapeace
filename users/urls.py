from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/users/$', views.UsersListView.as_view(), name='user_list_create_api'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserView.as_view(), name='user_update_delete_get_api'),
]
