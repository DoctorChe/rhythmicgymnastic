from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Competition
# from . import views

app_name = 'competitions'
urlpatterns = [
                url(r'^$', ListView.as_view(
                                    # queryset=Post.objects.all().order_by("-date")[:25],
                                    queryset=Competition.objects.all().order_by("title")[:25],
                                    template_name="competitions/competitions.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model=Competition,
                                    template_name="competitions/competition.html")),
                url(r'^(?P<pk>\d+)/rank$', DetailView.as_view(
                                    model=Competition,
                                    template_name="competitions/competition_rank.html")),
                url(r'^(?P<pk>\d+)/protocol$', DetailView.as_view(
                                    model=Competition,
                                    template_name="competitions/competition_protocol.html")),

                # url(r'^(?P<pk>\d+)/protocol_print$', views.protocolview),

                # url(r'^iii$', views.index),
                # url(r'^download$', views.render_pdf),
                # url(r'^download_pdf$', views.competition_pdf),

                # url(r'^$', views.post_list, name='post_list'),
                # url(r'^$', views.PostListView.as_view(), name='post_list'),
                # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/' \
                #     r'(?P<post>[-\w]+)/$',
                #     views.post_detail,
                #     name='post_detail'),
            ]
