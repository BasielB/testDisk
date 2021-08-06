from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .shell_logic import disks
from .request_handler import handler


@login_required
def show_disks(request):

    context = {
        'disks': disks.get_all_disks(),
        'title': 'SUPER ULTRA HARD DRIVER MANAGER 3000'
    }

    return render(request, template_name='main/drivers.html', context=context)


@login_required
def mount_disk(request):

    request_body = handler.extract_dict_from_body(request)

    if disks.mount_disk(request_body['name']) is False:
        return render(request, 'main/err_mount.html')

    return redirect('/disks/')


@login_required
def umount_disk(request):

    request_body = handler.extract_dict_from_body(request)
    disks.umount_disk(request_body['name'])

    return redirect('/disks/')


@login_required
def format_disk(request):

    request_body = handler.extract_dict_from_body(request)

    if disks.format_disk(request_body['name']) is False:
        return render(request, 'main/err_format.html')

    return redirect('/disks/')


@login_required
def redirect_to_home_page(request):

    return redirect('/disks/')
