"""
Used to register models to the admin page for the API app
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Tournament
from .models import TournamentUser
from .models import Match
from .models import MatchUser
from .models import Game

admin.site.register(User, UserAdmin)
admin.site.register(Tournament)
admin.site.register(TournamentUser)
admin.site.register(Match)
admin.site.register(MatchUser)
admin.site.register(Game)
