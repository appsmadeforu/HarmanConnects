from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from socialize import views


urlpatterns = [
    path('', views.index, name="index"),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    path('AddProject/', views.project, name='project'),
]