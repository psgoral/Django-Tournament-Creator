from django.shortcuts import render,redirect

from django.http import HttpResponse
from main.forms import newTournament,newComment
from django.contrib.auth.models import User
from main.models import Tournament,CheckIn,Match,Comment
from main.fun import *
import math


def index(response,id):
    return HttpResponse("HELLO")


def home(response):
    return render(response,'main/home.html')

def new(response):
    current_user = response.user

    if response.method == 'POST':
        form = newTournament(response.POST)
            
        new = form.save(commit=False)
        
        new.owner_id = current_user.id
        new.save()

        # if new.typ == "T":
        #     generateTournament(new)
        return redirect('/tournaments')
    else:
        form = newTournament()


    return render(response,'main/new.html',{'form' : form})

def tournaments(response):

    tournaments = Tournament.objects.all()

    current_user = response.user
    
    for t in tournaments:
        players = CheckIn.objects.filter(tournament=t.id).all()
        n_players = len(players)

        if CheckIn.objects.filter(player=User(id=current_user.id),tournament=t.id).count() == 1:
            t.checked = True
        t.actual = n_players
        t.players = players

    context = {
        'tournaments' : tournaments,
        

    }
    return render(response,'main/tournaments.html',context)


def join(response,t_id):

    current_user = response.user

    join = CheckIn(player=User(id=current_user.id),tournament=Tournament(id=t_id))
    join.save()

    playersIn = CheckIn.objects.filter(tournament=Tournament(id=t_id)).count()

    t = Tournament.objects.filter(id=t_id).get()
    print('IN:' + str(playersIn) + ' of ' + str(t.number_of_players))
    if playersIn == t.number_of_players:
        generateTournament(t)
    return redirect('/tournaments')

def leave(response,t_id):

    current_user = response.user

    leave = CheckIn.objects.filter(player=User(id=current_user.id),tournament=Tournament(id=t_id))
    leave.delete()
    return redirect('/tournaments')


def delete(response,t_id):

    t = Tournament.objects.filter(id=t_id).get()
    t.delete()

    return redirect('/tournaments')


def details(response):
    t_id = response.POST
    t = Tournament.objects.get(id=t_id)
    players = CheckIn.objects.filter(tournament=t.id)

    for player in players:
        print(player.player.account.username)

    context = {
        'tournament' : t,
        'players' : players,
    }
    return render(response,'main/details.html',context)



def add_score(response):
    if response.method == 'POST':
        match_id = response.POST['match_id']
        actual = Match.objects.filter(id=match_id)
        player_id = int(response.POST['player_id'])

        # if player_id == actual.player1.id:
        print("form player: " +str(player_id))
        print("p1: " + str(actual.get().player1.id))
        if player_id == actual.get().player1.id:
            score1byp1 = response.POST['score1']
            score2byp1 = response.POST['score2']
            actual.update(score1byp1=score1byp1,score2byp1=score2byp1)
        elif player_id == actual.get().player2.id:
            score1byp2 = response.POST['score1']
            score2byp2 = response.POST['score2']
            actual.update(score1byp2=score1byp2,score2byp2=score2byp2)

        if actual.get().score1byp1 == actual.get().score1byp2 and actual.get().score2byp1 == actual.get().score2byp2:
            score1 = actual.get().score1byp1
            score2 = actual.get().score2byp2
            actual.update(score1=score1,score2=score2)


        actual = Match.objects.filter(id=match_id).get()
        
        score1 = actual.score1
        score2 = actual.score2

        if score1 > score2:
            winner = actual.player1
        else:
            winner = actual.player2
        print('actual nr: ' + str(actual.match_number))
        if actual.match_number %2 !=0:
            next = math.ceil(0.1+ actual.match_number//2)
        else:
            next = actual.match_number//2
        print('round: ' + str(actual.round_number+1) + '    number: ' + str(next))

        if actual.match_number %2 ==1:
            nextmatch = Match.objects.filter(round_number=(actual.round_number+1),match_number=next)
            nextmatch.update(player1=winner)
            print('update!' + str(nextmatch))
        else:
            Match.objects.filter(round_number=(actual.round_number+1),match_number=next).update(player2=winner)


        return redirect('/match_' + str(match_id))
    return redirect('/match_' + str(match_id))
    
    


# current_user = response.user

#     if response.method == 'POST':
#         form = newTournament(response.POST)
            
#         new = form.save(commit=False)
        
#         new.owner_id = current_user.id
#         new.save()

#         # if new.typ == "T":
#         #     generateTournament(new)
#         return redirect('/tournaments')
#     else:
#         form = newTournament()


#     return render(response,'main/new.html',{'form' : form})




def match(response,match_id):

    current_user = response.user
    if response.method == 'POST':
        form = newComment(response.POST)

        new = form.save(commit=False)

        new.author = currend_user
        new.save()

        return redirect('/match_' + str(match_id))
    else:
        form = newComment()
        match = Match.objects.filter(id=match_id).get()

        
        context = {
            'match' : match,
            'form' : form
        }

        return render(response,'main/match.html',context)


def ladder(response,t_id):

    t = Tournament.objects.get(id=t_id)
    

    matches = Match.objects.filter(tournament=t_id).order_by('round_number','match_number').all()


    rounds = matches[len(matches)-1].round_number
    
    context = {
        'matches' : matches,
        'rounds' : range(1,rounds+1),
    }

    return render(response,'main/ladder.html',context)

def create_users(response):
    makeAcc()
    return HttpResponse("Konta utworzone!")

