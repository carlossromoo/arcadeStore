from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.db.models import Q
from .models import Games,Review
from .forms import ReviewForm, AgregarJuegoForm
# Create your views here.
class GamesListView(ListView):
    model = Games
    context_object_name = 'game_list'
    template_name = 'games/games_list.html'

class GamesDetailView(DetailView):
    model = Games
    context_object_name = 'games'
    template_name = 'games/games_detail.html'

class SearchResultsListView(ListView):
    model = Games
    context_object_name = "game_list"
    template_name = "games/search_results.html"
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Games.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )

class CreateReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    context_object_name = 'create_review'
    template_name = 'games/crear_review.html'
        
    def form_valid (self, form):
        form.instance.game_id= self.kwargs['game_id']
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('game_detail', kwargs={'pk': self.kwargs['game_id']})
        
class AgregarJuegoView(View):
    template_name = 'games/agregar_game.html'

    def get (self, request):
        form = AgregarJuegoForm()
        return render(request, self.template_name,{'form': form}) 
    
    def post(self, request):
        form = AgregarJuegoForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            return redirect(game.get_absolute_url())
        return render(request, self.template_name, {'form': form})
