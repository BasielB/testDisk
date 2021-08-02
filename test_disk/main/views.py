from django.shortcuts import render
from django.http import HttpResponse


def show_disks(request):

    disks = None

    context = {
        'disks': disks,
        'title': 'Диски'
    }

    return render(request, template_name='main/hello.html', context=context)
