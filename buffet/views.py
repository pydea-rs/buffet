from django.shortcuts import render
from food.models import Food


def home(request):
    foods = Food.objects.all().filter(available=True)

    context = {
        'foods': foods
    }
    return render(request, 'home.html', context)
