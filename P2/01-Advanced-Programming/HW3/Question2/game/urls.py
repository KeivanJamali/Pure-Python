from django.urls import path

from .views import authenticate, signup, profile, scoreboard

urlpatterns = [
    path('authenticate/', authenticate, name='authenticate'),
    path('signup', signup, name='signup'),
    path('profile/<str:username>', profile, name='profile'),
    path('scoreboard/', scoreboard, name='scoreboard'),
]
