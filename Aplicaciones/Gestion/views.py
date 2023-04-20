from django.shortcuts import render
from .models import Taludes


# Create your views here.
def home(request):
    taludesListados = Taludes.objects.all()
    return render(request, "GestionTaludes.html", {"cursos": taludesListados})
