#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import argparse


def crack_key(exe_path, key, fix):
    print(exe_path)
    with open(exe_path, 'rb') as f:
        data = f.read()

    for x in range(len(data) - len(key)):
        if data[x:x + len(key)] == key:
            print('Find and crack')
            bak_file = f'{exe_path}.bak'
            if not os.path.exists(bak_file):
                os.rename(exe_path, bak_file)
            else:
                os.remove(exe_path)
            print(f'Bak file: {bak_file}...', end='', flush=True)
            with open(exe_path, 'wb') as f:
                f.write(data[:x])
                f.write(fix)
                f.write(data[x + len(fix):])
            print('crack complete')
            break


def crack_xshell(exe_path):
    key_bytes = b'\x74\x11\x6A\x00\x6A\x07\x6A\x01'
    fix_bytes = b'\xeb' + key_bytes[:1]
    crack_key(exe_path, key_bytes, fix_bytes)


def crack_xftp(exe_path):
    key_bytes = b'\x75\x10\x6A\x00\x6A\x07\x50\x6A'
    fix_bytes = b'\xeb' + key_bytes[:1]
    crack_key(exe_path, key_bytes, fix_bytes)


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

        parser.add_argument('--xshell', metavar='<xshell.exe>', help='crack xshell')
        parser.add_argument('--xftp', metavar='<xftp.exe>', help='crack xftp')

        args = parser.parse_args()
        if args.xshell:
            crack_xshell(args.xshell)
        elif args.xftp:
            crack_xftp(args.xftp)
        else:
            parser.print_help()


if __name__ == '__main__':
    App.run()
