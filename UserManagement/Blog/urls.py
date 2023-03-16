from django.conf.urls import url
from .views import listing, view_blog,see_request, user_info,add_messages


app_name = 'blog'

urlpatterns = [
    url(r"^listing/", listing, name='listing'),
    url(r"^view_blog/(?P<blog_id>\d+)/$", view_blog, name = 'view_blog'),
    url(r"^see_request/", see_request, name = 'see_request'),
    url(r"^user_info/", user_info, name = 'user_info'),
    url(r"^add_messages/", add_messages, name = 'add_messages'),
]