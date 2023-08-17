from django.urls import re_path as url
from django.contrib.auth.decorators import login_required
from ecom import views


app_name = 'ecom'

urlpatterns = [
    url('register/', views.register, name='register'),
    url('user_login/', views.user_login, name='user_login'),
    # all blog at one page..
    url('blogs/', views.blogs, name='blogs'),

    # class based view
    url(r'my_blog/', login_required(views.BlogListView.as_view()), name='my_blog'),
    url(r'^create/$', login_required(views.BlogCreateView.as_view()), name='create'),
    url(r'^update/(?P<pk>\d+)/$', login_required(views.BlogUpdateView.as_view()), name='update'),
    # public blog
    url(r'^blog_details/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='blog_details'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.BlogDeleteView.as_view()), name='delete'),
    url(r'add-to-cart/(?P<pk>\d+)/$', views.add_to_cart_view,name='add-to-cart'),
    url(r'remove-from-cart/(?P<pk>\d+)/$',  views.remove_from_cart_view,name='remove-from-cart'),
    
]

