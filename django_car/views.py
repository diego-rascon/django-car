from django.shortcuts import render


def stopped(request):
    return render(request, 'stopped.html')


def forward(request):
    return render(request, 'forward.html')


def backward(request):
    return render(request, 'backward.html')


def left(request):
    return render(request, 'left.html')


def right(request):
    return render(request, 'right.html')
