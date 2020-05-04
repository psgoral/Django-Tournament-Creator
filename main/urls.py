from django.urls import path

from . import views


urlpatterns = [
    path("", views.home,name="home"),
    path("new", views.new,name="new"),
    path("tournaments", views.tournaments,name="tournaments"),
    path("join/<int:t_id>", views.join,name="join"),
    path("leave/<int:t_id>", views.leave,name="leave"),
    path("delete/<int:t_id>", views.delete,name="delete"),
    path("details", views.details,name="details"),
    path("match_<int:match_id>", views.match,name="match"),
    path("ladder_<int:t_id>", views.ladder,name="ladder"),
    path("add_score", views.add_score,name="add_score"),
    path("create_users", views.create_users,name="create_users"),



]