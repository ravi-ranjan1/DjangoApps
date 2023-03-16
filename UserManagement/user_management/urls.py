from django.conf.urls import url
from django.urls import include
from .views import dashboard, register


urlpatterns =[
    url(r"accounts/",include("django.contrib.auth.urls")),
    url(r"^dashboard/",dashboard, name="dashboard"),
    url(r"^register/", register, name='register'),

]