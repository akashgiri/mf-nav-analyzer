from django.conf.urls import url

from . import views

app_name = "funds_info"
urlpatterns = [
    url(r'^fund$', views.show_funds_list, name='index'),
]
