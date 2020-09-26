from django.shortcuts import render

# Create your views here.
from .models import Music, Author, MusicInstance, Genre


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_musics = Music.objects.all().count()
    num_instances = MusicInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = MusicInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_musics': num_musics, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors, "num_visits": num_visits},
    )

from django.views import generic


class MusicListView(generic.ListView):
    model = Music

class MusicDetailView(generic.DetailView):
    model = Music

"""
from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import RenewMusicForm


@permission_required('catalog.can_mark_returned')
def renew_music_librarian(request, pk):
    music_inst = get_object_or_404(MusicInstance, pk=pk)

    if request.method == 'POST':

        form = RenewMusicForm(request.POST)

        if form.is_valid():
            music_inst.due_back = form.cleaned_data['renewal_date']
            music_inst.save()

            return HttpResponseRedirect(reverse('all-borrowed'))


    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewMusicForm(initial={'renewal_date': proposed_renewal_date, })

    return render(request, 'catalog/music_renew_librarian.html', {'form': form, 'musicinst': music_inst})

"""