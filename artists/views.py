from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ArtistForm


# Create your views here.
def index(request):
    return HttpResponse('Artists')


def album_form(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artists/')
    else:
        form = ArtistForm()

    return render(request, 'artist_form.html', {'form': form})
