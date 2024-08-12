from django.urls import path, include
from memo import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('route', views.home, name='dashboard'),
    path('message', views.message_func, name='message'),
    path('details/<int:pk>', views.detail_func, name='details'),
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]