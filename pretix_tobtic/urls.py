from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^test/info', views.ShowPageView.as_view(),  name="all-orgs"),
    url(r'^pages/info', TemplateView.as_view(template_name='tobtic_info.html'), name="index"),
    url(r'^pages/arranger', TemplateView.as_view(template_name='tobtic_arranger.html'), name="index"),
    url(r'^pages/terms', TemplateView.as_view(template_name='tobtic_terms.html'), name="index"),
    url(r'^$', views.ShowPageView.as_view(template_name='tobtic_index.html'), name="index")
]