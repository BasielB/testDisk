from django.urls import path
from .views import *


urlpatterns = [
    path('', show_disks, name='home'),
    path('mount', mount_disk, name='mount'),
    path('umount', umount_disk, name='umount'),
    path('format', format_disk, name='format')
]
