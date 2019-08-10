"""
URLs for the API

Note that all the paths below are preceded by
/api/
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views
from . import views

urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('tournaments/', views.TournamentList.as_view(), name='tournament-list'),
    path('tournaments/<int:pk>', views.TournamentDetail.as_view(), name='tournament-detail'),
    path('tournament_users/', views.TournamentUserList.as_view(), name='tournamentuser-list'),
    path('tournament_users/<int:pk>',
         views.TournamentUserDetail.as_view(),
         name='tournamentuser-detail'),
    path('matches/', views.MatchList.as_view(), name='match-list'),
    path('matches/<int:pk>', views.MatchDetail.as_view(), name='match-detail'),
    path('match_users/', views.MatchUserList.as_view(), name='matchuser-list'),
    path('match_users/<int:pk>', views.MatchUserDetail.as_view(), name='matchuser-detail'),
    path('games/', views.GameList.as_view(), name='game-list'),
    path('games/<int:pk>', views.GameDetail.as_view(), name='game-detail'),
    path('api-token-auth/', auth_views.obtain_auth_token, name='get-token'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
