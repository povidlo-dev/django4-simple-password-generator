from django.shortcuts import render
import random
# from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    chars = list(map(chr, range(97, 123)))
    length = int(request.GET.get('length', 12))
    generated_password = ''

    if request.GET.get('uppercase'):
        chars.extend(list(map(chr, range(65, 91))))

    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))

    for i in range(length):
        generated_password += random.choice(chars)

    return render(request, 'generator/password.html', {'password': generated_password})


def about(request):
    return render(request, 'generator/about.html')
