from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

app_name = "funds_info"
urlpatterns = [
    url(r'^$', views.show_funds_list, name='show_funds_list'),
    #url(r'^fund/$', views.show_funds_list, name='show_funds_list'),
    url(r'^fund/nav_change/', views.get_nav_change, name='get_nav_change'),    
    url(r'^fund/(?P<page_slug>[\w-]+)/', views.show_all_stocks, name='show_all_stocks'),
]
