from django.conf.urls import url
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    path('',views.home, name = 'home'),
    path('new/profile', views.add_profile, name='edit'),
    path('myprofile',views.my_profile, name ='myprofile'),
    path('addhood',views.addhood, name='addhood'),
    path('detail/(?P<neighbourhood_id>\d+)/',views.neighbourhood_details, name='detail'),
    path('new_business/(?P<pk>\d+)/' , views.new_business,name='new_business'),
    path('new_post/(?P<pk>\d+)', views.new_post, name='new_post'),
    path('search/', views.search_project, name='search'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)