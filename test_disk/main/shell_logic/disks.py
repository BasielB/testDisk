import subprocess
import os


def get_all_disks():

    # all_disks = []
    #
    # shell_result = subprocess.run(['lsblk', ], stdout=subprocess.PIPE)
    # rows = shell_result.stdout.decode('utf-8').split('\n')
    #
    # for i in range(1, len(rows)-1):
    #     split_row = rows[i].split()
    #
    #     if 'disk' in split_row:
    #         name = split_row[0]
    #         size = split_row[3]
    #         try:
    #             mount_point = split_row[6]
    #         except IndexError:
    #             mount_point = None
    #         disk = {
    #             'name': name,
    #             'size': size,
    #             'mount_point': mount_point
    #         }
    #
    #         all_disks.append(disk)

    # return all_disks

    return [{'name': 'sda',
             'size': '8G',
             'mount_point': None},
            {'name': 'sdb',
             'size': '4G',
             'mount_point': None},
            {'name': 'sdc',
             'size': '2G',
             'mount_point': '/'}
            ]


def mount_disk(name: str):
    sudo_password = 'butovich'
    command_mkdir = f'mkdir /mnt/{name}'
    command_mount = f'mount /dev/{name} /mnt/{name}'

    # subprocess.run(['echo', f'{sudo_password}', '|', 'sudo', '-S', 'mkdir', f'/mnt/{name}'])
    os.system(f'echo {sudo_password}|sudo -S {command_mkdir}')
    os.system(f'echo {sudo_password}|sudo -S {command_mount}')


def umount_disk(name: str):
    pass


if __name__ == "__main__":
    mount_disk('sdc_test')
