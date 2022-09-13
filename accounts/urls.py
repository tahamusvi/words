from django.urls import path
from . import views as viewsA


app_name= 'accounts'


urlpatterns = [
    path('profile/', viewsA.Profile.as_view() ,name='profile'),
    path('َUsers/PasswordChangeView',viewsA.PasswordChangeView.as_view(),name='PasswordChangeView'),
    path('login/',viewsA.Login.as_view(),name="Login"),

]
