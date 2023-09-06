from django.urls import path
from . import views

urlpatterns = [
    path('comp_detail/', views.comp_detail, name='comp-detail'),
    path('currentcomps/', views.currentcomps, name='current-comps'),
    path('related/', views.related, name='related'),
    path('winners/', views.winners, name='winners'),
]
