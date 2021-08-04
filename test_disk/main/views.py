from django.shortcuts import render
from django.http import HttpResponse

from .shell_logic.disks import get_all_disks
import json


def show_disks(request):

    context = {
        'disks': get_all_disks(),
        'title': 'Диски'
    }

    return render(request, template_name='main/hello.html', context=context)


def mount_disk(request):

    body = request.body.decode('utf-8').split('&')
    body = {i.split('=')[0]: i.split('=')[1] for i in body}

    print(body['name'])

    return render(request, template_name='main/hello.html', context=context)
