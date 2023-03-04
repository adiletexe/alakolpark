from django.contrib import admin
from django.urls import path
from check.views import check_availability, make_booking, index, prices, map1, contacts, add_review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('prices', prices, name='prices'),
    path('map', map1, name='map'),
    path('contacts', contacts, name='contacts'),
    path('check_availability/', check_availability, name='check_availability'),
    path('make_booking/', make_booking, name='make_booking'),
    path('add/', add_review, name='add_review'),
]
