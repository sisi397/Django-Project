from django.urls import path

from . import views



urlpatterns = [
    path('', views.index),
    
    path('signup', views.signup),

    path('login', views.login),
    
    path('snack', views.index_snack),
    
    path('bot', views.bot),
    
    path('bak', views.bak),
    
    path('meat', views.index_meat),
    
    path('fish', views.fish),
    path('egg', views.egg),
    path('fruits', views.index_fruits),
    path('veg', views.veg),
    path('rice', views.index_rice),
    path('rice2', views.rice2),
    path('freeze', views.freeze),
    path('all', views.all),
    path('shipment', views.shipment),
    path('introduction', views.introduction),
    path('foruser', views.foruser),
    path('howto', views.howto),
    path('guide', views.guide),
   ]
