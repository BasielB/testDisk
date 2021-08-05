from django.shortcuts import render, redirect

from .shell_logic import disks
from .request_handler import handler


def show_disks(request):

    context = {
        'disks': disks.get_all_disks(),
        'title': 'Диски'
    }

    return render(request, template_name='main/hello.html', context=context)


def mount_disk(request):

    request_body = handler.extract_dict_from_body(request)

    disks.mount_disk(request_body['name'])

    return redirect('/disks/')


def umount_disk(request):

    request_body = handler.extract_dict_from_body(request)

    disks.umount_disk(request_body['name'])

    return redirect('/disks/')


def format_disk(request):

    request_body = handler.extract_dict_from_body(request)

    disks.format_disk(request_body['name'])

    return redirect('/disks/')
