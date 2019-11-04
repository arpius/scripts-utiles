#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

repository = 'sftp:gominola:/media/storage/backups'


def show():
    subprocess.run(
        ['restic', '-r', repository, 'snapshots'],
        check=True)


def backup(target):
    subprocess.run(
        ['restic', '-r', repository, 'backup', '--verbose', target],
        check=True)


def remove(target):
    subprocess.run(
        ['restic', '-r', repository, 'forget', target],
        check=True)


def prune(copies=1):
    subprocess.run(
        ['restic', '-r', repository, 'forget',
            '--keep-last={}'.format(copies), '--prune'],
        check=True)


def restore(snapshot, target):
    subprocess.run(
        ['restic', '-r', repository, 'restore', snapshot, '--target', target],
        check=True)


def menu():
    subprocess.run('clear')

    title = ' Backing up with Restic '
    op1 = '1) List snapshots.'
    op2 = '2) Make a backup.'
    op3 = '3) Delete backup.'
    op4 = '4) Reduce the amount of snapshots.'
    op5 = '5) Restore from a snapshot.'
    op6 = '6) Exit.'

    menu = '{:-^42}\n {}\n {}\n {}\n {}\n {}\n {}'.format(
        title, op1, op2, op3, op4, op5, op6)

    print(menu)


def main():
    while True:
        menu()
        option = input("\nChoose an option: ")
        continue_text = "Press the <ENTER> key to continue..."

        if option == '1':
            show()
            input(continue_text)
        elif option == '2':
            target = input("Insert backup's target: ")
            backup(target=target)
            input(continue_text)
        elif option == '3':
            target = input("Insert the ID of the snapshot to be deleted: ")
            remove(target=target)
            input(continue_text)
        elif option == '4':
            copies = input("Insert the number of copies to be kept: ")
            prune(copies=copies)
            input(continue_text)
        elif option == '5':
            snapshot = input("Insert the ID of the snapshot to be restored: ")
            target = input("Insert where it will be restored: ")
            restore(snapshot=snapshot, target=target)
            input(continue_text)
        elif option == '6':
            print("See you!")
            break
        else:
            print("Incorrect option!")


if __name__ == "__main__":
    main()
