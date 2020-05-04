from django.forms import ModelForm
from main.models import Match,Tournament


class newTournament(ModelForm):

    class Meta:
        model = Tournament
        fields = ['name','number_of_players','typ']

        def set_owner(self,id):
            self.owner_id = id 



