from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # re_path(r"(?P<coordination>-?\d+\.?\d*)", views.geturl, name='geturl') can only get the first number

    # pass the parameters by Get
    path('cal', views.geturl, name='geturl'),

]