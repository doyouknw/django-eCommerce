from django.conf.urls import url
from .views import Home
from django.views.generic import TemplateView

# urlpatterns = [
#     url(r'^$', views.index, name="home"),
# ]
urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
]