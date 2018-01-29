from django.conf.urls import url
from core import views


urlpatterns = [
    url(r'^core/$', views.CardList.as_view()),
    url(r'^core/(?P<id>[0-9]+)/$', views.CardDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<id>[0-9]+)/$', views.UserDetail.as_view()),
]
