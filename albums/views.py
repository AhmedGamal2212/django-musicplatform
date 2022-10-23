from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AlbumForm


# Create your views here.
def index(request):
    return HttpResponse('Albums')


def album_form(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/albums/')
    else:
        form = AlbumForm()

    return render(request, 'album_form.html', {'form': form})
