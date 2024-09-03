
from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='news'),
    path('news/create_news', views.create_news, name='add_news'),

]