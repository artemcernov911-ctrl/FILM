from django.shortcuts import render
from .models import Films
from .forms import News_Films

def films(request):
    if request.method == 'POST':
        form = News_Films(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Данные были заполнены некорректно"
            return render(request, 'films/add.html', {'form': form, 'error': error})
    else:
        form = News_Films()
    return render(request, 'films/add.html', {'form': form})

def pub(request):
    films = Films.objects.all()
    return render(request, 'films/pub.html', {'films': films})