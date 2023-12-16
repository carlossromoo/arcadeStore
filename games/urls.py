from django.urls import path
from .views import GamesListView, GamesDetailView, SearchResultsListView,CreateReviewView,AgregarJuegoView

urlpatterns = [
    path("", GamesListView.as_view(), name="game_list"),
    path("<uuid:pk>/", GamesDetailView.as_view(), name="game_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("create_review/<uuid:game_id>/", CreateReviewView.as_view(), name="create_review"),
    path("agregar_game/", AgregarJuegoView.as_view(), name="agregar_game"),
]