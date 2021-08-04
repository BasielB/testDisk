from django.urls import path
from .views import *


urlpatterns = [
    path('', show_disks),
    path('mount', mount_disk, name='mount'),
    path('umount', umount_disk, name='umount')
]
