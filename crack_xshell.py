#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import argparse

# pip install elevate
# from elevate import elevate


def do_crack_app(app_path, key, fix):
    print(f'Crack {app_path}')
    bak_file = f'{app_path}.bak'

    with open(app_path, 'rb') as f:
        data = f.read()

    for x in range(len(data) - len(key)):
        if data[x:x + len(key)] == key:
            print(f'Bak file: {bak_file}')
            if not os.path.exists(bak_file):
                os.rename(app_path, bak_file)
            else:
                os.remove(app_path)
            with open(app_path, 'wb') as f:
                f.write(data[:x])
                f.write(fix)
                f.write(data[x + len(fix):])
            print('crack complete')
            return
    print('Please check version!')


def crack_xshell(app_path):
    key_bytes = b'\x74\x11\x6A\x00\x6A\x07\x6A\x01'
    fix_bytes = b'\xeb' + key_bytes[:1]
    do_crack_app(app_path, key_bytes, fix_bytes)


def crack_xftp(app_path):
    key_bytes = b'\x75\x10\x6A\x00\x6A\x07\x50\x6A'
    fix_bytes = b'\xeb' + key_bytes[:1]
    do_crack_app(app_path, key_bytes, fix_bytes)


def crack_app(app):
    # elevate()

    print(app)
    app2 = app.lower()
    if app2.endswith('xshell.exe'):
        crack_xshell(app)
    elif app2.endswith('xftp.exe'):
        crack_xftp(app)
    else:
        print(f'Unknown app: {app}')
    input('<>')


def crack_stdin():
    in_file = input('Xshell/Xftp: ')
    crack_app(in_file)


class App():
    name = 'Crack Xshell/Xftp'
    description = ''
    version = '1.0'
    url = ''
    author_email = 'unknown@gmail.com'
    license = 'MIT'

    @classmethod
    def run(cls):
        about = f'{App.name} v{App.version} {App.description}'
        parser = argparse.ArgumentParser(description=App.description)
        parser.add_argument('--version', action='version', version=about,
                            help='show version')

        parser.add_argument('app', metavar='Xshell/Xftp', nargs='?', help='crack Xshell/Xftp')

        args = parser.parse_args()
        if args.app:
            crack_app(args.app)
        else:
            crack_stdin()


if __name__ == '__main__':
    App.run()
