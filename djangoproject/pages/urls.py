
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
path('login/', views.login, name='login'),
path('upload/', views.upload, name='upload'),
path('house_list/', views.house_list, name='house_list'),
path('upload_house/', views.upload_house, name='upload_house'),
path('searched/', views.searched, name='searched'),

path('house_list/<int:pk>/', views.delete_house, name='delete_house'),
path('search/', views.search, name='search'),

path('register/', views.register, name='register'),
path('register_submission/', views.register_submission, name='register_submission'),
path('login_submission/', views.login_submission, name='login_submission'),

path('single_list/', views.single_list, name='single_list'),
path('blog/', views.blog, name='blog'),
path('contact/', views.contact, name='contact'),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



