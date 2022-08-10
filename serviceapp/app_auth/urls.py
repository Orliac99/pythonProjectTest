from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_service, name="login"),
    path('register/', views.register_view, name="register"),
    path('', views.log_out, name="logout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]