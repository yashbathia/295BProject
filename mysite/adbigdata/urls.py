from django.conf.urls import patterns, url

from adbigdata import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^advertiser/(?P<adv_name>\D+)/$', views.detail, name='detail'),
    url(r'^advertiser_registration/$', views.adv_reg, name='adReg'),
    url(r'^eventOrganizer_registration/$', views.eOrg_reg, name='eOrgReg'),
)
