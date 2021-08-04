from django.shortcuts import render, redirect
from django.http import HttpResponse

from .shell_logic import disks
import json


def show_disks(request):

    context = {
        'disks': disks.get_all_disks(),
        'title': 'Диски'
    }

    return render(request, template_name='main/hello.html', context=context)


def mount_disk(request):

    body = request.body.decode('utf-8').split('&')
    body = {i.split('=')[0]: i.split('=')[1] for i in body}

    disks.mount_disk(body['name'])

    return redirect('disks/')


def umount_disk(request):

    body = request.body.decode('utf-8').split('&')
    body = {i.split('=')[0]: i.split('=')[1] for i in body}

    disks.umount_disk(body['name'])

    return redirect('disks/')
