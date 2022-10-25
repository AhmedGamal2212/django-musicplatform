from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView

from .forms import ArtistForm
from .models import Artist


class ArtistList(ListView):
    model = Artist


class ArtistFormView(LoginRequiredMixin, FormView):
    success_url = '/artists/'
    form_class = ArtistForm
    template_name = 'artists/artist_form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
