from django.conf.urls import patterns, url

from visits import views

urlpatterns = patterns('',
                       url(r'^$', views.VisitList.as_view(), name="index"),
                       url(r'^(?P<pk>\d+)/$', views.VisitDetail.as_view(), name="detail"),
                       )
