from django.urls import path

from users.views import enter_or_registration, profile, logout

app_name = 'users'

urlpatterns = [
    path('enter_or_registration/', enter_or_registration, name='enter_or_registration'),
    path('profile/', profile , name='profile'),
    path('logout/', logout , name='logout')


]