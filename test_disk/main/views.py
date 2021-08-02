from django.shortcuts import render
from django.http import HttpResponse

from .shell_logic.disks import get_all_disks


def show_disks(request):

    context = {
        'disks': get_all_disks(),
        'title': 'Диски'
    }

    return render(request, template_name='main/hello.html', context=context)
