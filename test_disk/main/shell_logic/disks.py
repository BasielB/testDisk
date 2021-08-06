import subprocess
import os


def get_all_disks():

    all_disks = []

    shell_result = subprocess.run(['lsblk', ], stdout=subprocess.PIPE)  # Take stdout
    rows = shell_result.stdout.decode('utf-8').split('\n')  # Make list with rows from stdout

    for i in range(1, len(rows)-1):
        split_row = rows[i].split()  # Make list with drivers parameters from stdout row

        if 'disk' in split_row:  # Take row with only disk in future result
            name = split_row[0]
            size = split_row[3]
            try:  # Cause disk may be not mounted
                mount_point = split_row[6]
            except IndexError:
                mount_point = None
            disk = {
                'name': name,
                'size': size,
                'mount_point': mount_point
            }

            all_disks.append(disk)

    return all_disks

    # TEST RETURN
    # return [{'name': 'sda',
    #          'size': '8G',
    #          'mount_point': None},
    #         {'name': 'sdb',
    #          'size': '4G',
    #          'mount_point': None},
    #         {'name': 'sdc',
    #          'size': '2G',
    #          'mount_point': '/'}
    #         ]


def mount_disk(name: str):
    sudo_password = 'butovich'
    command_mkdir = f'mkdir /mnt/{name}'
    command_mount = f'mount /dev/{name} /mnt/{name}'

    os.system(f'echo {sudo_password}|sudo -S {command_mkdir}')

    if os.system(f'echo {sudo_password}|sudo -S {command_mount}') == 0:
        return True
    else:
        return False


def umount_disk(name: str):
    sudo_password = 'butovich'
    command_umount = f'umount /dev/{name}'

    os.system(f'echo {sudo_password}|sudo -S {command_umount}')


def format_disk(name: str):
    sudo_password = 'butovich'
    command_format = f'mkfs /dev/{name}'

    if os.system(f'echo {sudo_password}|sudo -S {command_format}') == 0:
        return True
    else:
        if os.system(f'echo {sudo_password}|sudo -S {command_format}|y') == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    print(format_disk('sda'))
    print(format_disk('sdc'))
