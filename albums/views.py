from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AlbumForm
from artists.models import Artist


# Create your views here.
class AlbumList(ListView):
    model = Artist

