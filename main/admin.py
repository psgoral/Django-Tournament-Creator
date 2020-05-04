from django.contrib import admin

from main.models import Tournament,Match,CheckIn



class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name','number_of_players','typ','owner')

class MatchAdmin(admin.ModelAdmin):
    list_display = ('round_number','match_number','player1','player2','tournament','score1','score2')

class CheckInAdmin(admin.ModelAdmin):
    list_display = ('player','tournament')
    

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(CheckIn, CheckInAdmin)


