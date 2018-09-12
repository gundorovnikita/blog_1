from django.shortcuts import render, redirect


def homepage(request):
    user = request.user
    return render(request, 'homepage.html', {'user': user})
