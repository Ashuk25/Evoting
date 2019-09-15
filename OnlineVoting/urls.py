from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index1, name="index"),
    path("party", views.party_image_view, name="party"),
    path("Election", views.Election, name="Election"),
    path("help", views.help, name="help"),
    path("voting", views.voting, name="voting"),
    path("party_info", views.party_info, name="party_info"),
    path("party_del", views.party_del, name="party_del"),
]
