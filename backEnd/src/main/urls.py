# @Author: andreacasino
# @Date:   2017-09-14T22:17:19+01:00
# @Last modified by:   andreacasino
# @Last modified time: 2017-09-17T19:03:16+01:00

from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^palindrome/$',views.palindrome_contact,name="contact"),
    url(r'^palindrome/(?P<page>[0-9]+)/$',views.page,name="page")
]
