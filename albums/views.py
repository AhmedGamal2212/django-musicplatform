from django.views.generic import ListView, FormView

from .forms import AlbumForm
from artists.models import Artist


# Create your views here.
class AlbumList(ListView):
    model = Artist
    template_name = 'albums/album_list.html'


class AlbumFormView(FormView):
    form_class = AlbumForm
    success_url = '/albums/'
    template_name = 'albums/album_form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
