from django.conf.urls import url
from image_hover import views

app_name = "image_hover"

urlpatterns = [
    url(r'^images/$', views.hover_image, name='images'),
    url(r'^$', views.welcome, name='welcome'),
]