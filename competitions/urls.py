from django.urls import path
from . import views

urlpatterns = [
    path('comp_detail/<product_id>', views.comp_detail, name='comp-detail'),
    path('currentcomps/', views.currentcomps, name='current-comps'),
    path('related/', views.related, name='related'),
    path('winners/', views.winners, name='winners'),
    path('createcomp/<user_id>', views.createcomp, name='create-comp'),
    path('my_competitions', views.my_competitions, name='my-competitions'),
    path('my_tickets', views.my_tickets, name='my-tickets'),
    path('latest', views.latest, name='latest'),
]


