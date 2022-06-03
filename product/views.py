from django.shortcuts import render
from .models import Drink, Category

# Create your views here.


def main(request):
    if request.method == "GET":
        categorys = Category.objects.all()
        return render(request, 'index.html', {'categorys':categorys})
    if request.method == "POST":
        category = request.POST.get('category')
        print(category)

        drinks = Drink.objects.filter(category=category)
        categorys = Category.objects.all()
        return render(request, 'index.html', {'drinks': drinks,'categorys':categorys})