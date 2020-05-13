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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.view import hello, current_datetime, hours_ahead, test_for, mypage, book_tender_info, display_meta, contact
from mysite import view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^anather-time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^for', test_for),
    url(r'^mypage', mypage),
    # url(r'^tender/$', book_tender_info),
    url(r'^tender/$', view.book_tender_info_page),
    url(r'^display/$', display_meta),
    url(r'^search-form/$', view.search_form),
    url(r'^search/$', view.search),
    url(r'^contact/$', view.contact),
    url(r'^title/$', view.title),
]
