from django.urls import path
from . import views

app_name='Akun'

urlpatterns = [
    path('',views.pendaftaran ,name='index'),
    path('login/',views.login ,name='login'),
]