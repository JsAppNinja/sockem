from django.contrib import admin
from .models import User
from .models import Tournament
from .models import TournamentUser
from .models import TournamentJudge
from .models import Match
from .models import MatchUser
from .models import Game

# Register your models here.
admin.site.register(User)
admin.site.register(Tournament)
admin.site.register(TournamentUser)
admin.site.register(TournamentJudge)
admin.site.register(Match)
admin.site.register(MatchUser)
admin.site.register(Game)