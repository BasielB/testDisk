import subprocess


def get_all_disks():

    all_disks = []

    shell_result = subprocess.run(['lsblk', ], stdout=subprocess.PIPE)
    rows = shell_result.stdout.decode('utf-8').split('\n')

    for i in range(1, len(rows)-1):
        split_row = rows[i].split()

        if 'disk' in split_row:
            name = split_row[0]
            size = split_row[3]
            try:
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


if __name__ == "__main__":
    print(get_all_disks())
