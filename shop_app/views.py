from django.shortcuts import render
from .models import Shop

def shop(request):
    print('Shop')
    if request.POST:
        shopp = Shop()
        shopp.email = request.POST.get('email')
        shopp.number = request.POST.get('number')
        shopp.name = request.POST.get('name')
        shopp.familya = request.POST.get('familya')
        print(shopp.name, shopp.familya, shopp.email, shopp.number)
        shopp.save()
    return render(request, "index.html")

