from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ArtistForm
from .models import Artist


def index(request):
    return render(request, 'index.html', {'artist_list': Artist.objects.all()})


def album_form(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artists/')
    else:
        form = ArtistForm()

    return render(request, 'artist_form.html', {'form': form})
