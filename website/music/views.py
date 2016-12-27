from django.shortcuts import render, get_object_or_404
from models import Album

def index(request):
	all_albums= Album.objects.all()
	context = {'all_albums' : all_albums}
	return render(request, 'music/index.html', context)

def detail(request,album_id):
	album = get_object_or_404(Album, id=album_id)
	return render(request, 'music/details.html', {'album' : album})

def favorite(request,album_id):
	album = get_object_or_404(Album, id=album_id)
	try:
		selected_song=album.song_set.get(id=request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/details.html', {'album' : album, error_message:"You didn't select a valid song"})
	else:
		selected_song.is_favourite = True
		selected_song.save()
		return render(request, 'music/details.html', {'album' : album})