from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from competitions.models import Post
from .models import Competition, Apparatus, Group

urlpatterns = [
                url(r'^$', ListView.as_view(
                                    # queryset=Post.objects.all().order_by("-date")[:25],
                                    queryset=Competition.objects.all().order_by("title")[:25],
                                    template_name="competitions/competitions.html")),
                # url(r'^(?P<pk>\d+)$', DetailView.as_view(
                #                     model = Post,
                #                     template_name="competitions/post.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = Competition,
                                    template_name="competitions/competition.html")),
            ]