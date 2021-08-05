from django.urls import path
from .views import *


urlpatterns = [
    path('', redirect_to_home_page),
    path('disks/', show_disks, name='home'),
    path('disks/mount', mount_disk, name='mount'),
    path('disks/umount', umount_disk, name='umount'),
    path('disks/format', format_disk, name='format')
]
