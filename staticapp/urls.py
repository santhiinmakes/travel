from django.urls import path
from . import views
app_name='staticapp'
urlpatterns = [

    path('', views.index, name="index"),

]
