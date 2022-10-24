from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView

from .forms import AlbumForm
from artists.models import Artist


# Create your views here.
class AlbumList(ListView):
    model = Artist
    template_name = 'albums/album_list.html'


def album_form(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/albums/')
    else:
        form = AlbumForm()

    return render(request, 'album_form.html', {'form': form})
