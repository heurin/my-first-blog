from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    path('', views.post_list, name='post_list'),
]
