import subprocess


def get_all_disks():

    all_disks = {}

    shell_result = subprocess.run(['lsblk', ], stdout=subprocess.PIPE)

    rows = shell_result.stdout.decode('utf-8').split('\n')

    for i in range(1, len(rows)-1):
        print(rows[i].split())

    return all_disks


if __name__ == "__main__":
    get_all_disks()
