from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.service, name="service"),
    path('acteur/', views.acteur, name="acteur"),
    path('detail/', views.detail, name="detail"),
    path('carreleur/', views.carreleur, name='carreleur'),
    path('electricien/', views.electricien, name='electricien'),
    path('menuisier/', views.menuisier, name='menuisier'),
    path('peintre/', views.peintre, name='peintre'),
    path('plombier/', views.plombier, name='plombier'),
    path('vitrier/', views.vitrier, name='vitrier'),
]