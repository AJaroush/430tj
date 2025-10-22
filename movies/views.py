from django.shortcuts import render, redirect, get_object_or_404
from django.db.utils import OperationalError, ProgrammingError
from .models import Video
from .forms import VideoForm


def video_list(request):
    """
    Safe list view:
    - If the DB/tables aren't ready yet (fresh container), don't crash.
    - Shows a gentle message via 'pending_migrations' flag that the DB
      is being initialized, and renders an empty list instead.
    """
    pending_migrations = False
    videos = []
    try:
        qs = Video.objects.all()
        # Touch the DB to detect "no such table" early
        _ = qs[:1].exists()
        videos = qs
    except (OperationalError, ProgrammingError):
        pending_migrations = True

    return render(
        request,
        'movies/video_list.html',
        {'videos': videos, 'pending_migrations': pending_migrations}
    )


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'movies/video_detail.html', {'video': video})


def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'movies/video_form.html', {'form': form})


def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm(instance=video)
    return render(request, 'movies/video_form.html', {'form': form})


def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('video_list')
    return render(request, 'movies/video_confirm_delete.html', {'video': video})
