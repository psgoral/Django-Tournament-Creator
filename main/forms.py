from django.forms import ModelForm
from main.models import Match,Tournament,Comment


class newTournament(ModelForm):

    class Meta:
        model = Tournament
        fields = ['name','number_of_players','typ']

        def set_owner(self,id):
            self.owner_id = id 


class newComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

        def set_rest(self,user_id,match_id):
            self.author = user_id
            self.match = match_id


