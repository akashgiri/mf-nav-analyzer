from django.conf.urls import url

from . import views

app_name = "funds_info"
urlpatterns = [
    url(r'^fund$', views.show_funds_list, name='show_funds_list'),
    url(r'^fund/(?P<page_slug>[\w-]+)/', views.show_all_stocks, name='show_all_stocks'),    
]
