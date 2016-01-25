"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from blog.views import index, show_genres, post_list

from blog.views import CategoryListView
from books.views import BookListView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #### Blog #######
    url(r'^$', 'blog.views.index'),
    url(r'^genres/$', 'blog.views.show_genres'),
    url(r'^blog/', 'blog.views.post_list'),
    url(r'^meta/', 'blog.views.display_meta'),
    url(r'^time/$', 'blog.views.current_datetime'),
    url(r'^time/plus/(\d{1,2})/$', 'blog.views.hours_ahead'),
    url(r'^products/$', CategoryListView.as_view()),
    url(r'^some_view/$','blog.views.some_view'),

    #### Books #######
#    url(r'^search-form/$', 'books.views.search_form'),
    url(r'^search/$', 'books.views.search'),
    url(r'^contact/$', 'books.views.contact'),
    url(r'^books/$', BookListView.as_view()),

]
