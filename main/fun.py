from main.models import Match,Tournament,CheckIn
import math
from django.contrib.auth.models import User
import random


# def matches_in_rounds(n,rounds):

#     roundsTab = []
#     left = n
#     for x in range(rounds):
#         left = left/2
#         roundsTab.append(range(int(left)))
        
#     return(roundsTab)



# def calculate_rounds(n):

#     left = n
#     rounds = 0
#     while left != 1:
#         rounds = rounds + 1
#         left = left - left/2
#         print(left)
#     return rounds
def makeAcc():

    names = ['mateusz','admin','boss','noob']
    for name in names:
        user=User.objects.create_user(name, password='mat123')
        user.is_superuser=True
        user.is_staff=True
        user.save()

def generateTournament(Tournament):

    n = Tournament.number_of_players


    playersAll = CheckIn.objects.filter(tournament=Tournament.id).all()

    players = []
    for player in playersAll:
        players.append(player.player.id)
    print(players)
    random.shuffle(players)


    left = n//2
    round_number = 1
    while left > 0:
        for x in range(1,left+1):
            if round_number == 1:
                player1 = players.pop()
                player2 = players.pop()
                new = Match(round_number=round_number,match_number=x,player1=User(id=player1),player2=User(id=player2),tournament=Tournament,score1=0,score2=0)
                new.save()
            else:
                new = Match(round_number=round_number,match_number=x,tournament=Tournament,score1=0,score2=0)
                new.save()
        left = left//2
        round_number = round_number + 1

    print('TOURNAMENT GENERATED')
    

