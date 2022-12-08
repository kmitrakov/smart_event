from django.urls import path

from .views import *

urlpatterns = [
    path('', EventIndex.as_view(), name='index'),
    path('event/<int:event_id>/', events, name='events'),
    path('about/', about, name='about'),
    path('eventadd/', event_add, name='event_add'),
    path('contact/', contact, name='contact'),
    path('signin/', sign_in, name='sign_in'),
    path('signout/', sign_out, name='sign_out'),
    path('myspace/', my_space, name='my_space')
]
