#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import argparse
import os
import sys

import pythoncom
from win32com.shell import shell


def create_shortcut(file_path, lnk_path=None, icon=None):
    if not lnk_path:
        name = os.path.basename(file_path).splitext()[0]
        lnk_path = '%s.lnk' % name
    if not icon:
        icon = file_path

    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink
    )

    shortcut.SetPath(file_path)
    shortcut.SetDescription("Python %s" % sys.version)
    shortcut.SetIconLocation(icon, 0)

    persist_file = shortcut.QueryInterface(pythoncom.IID_IPersistFile)
    persist_file.Save(lnk_path, 0)


class App():
    name = 'Shortcut'
    description = 'Create Shortcut'
    version = '1.0'
    url = ''
    author_email = 'author@gmail.com'
    license = 'MIT'

    @classmethod
    def run(cls):
        about = f'{App.name} v{App.version} {App.description}'
        parser = argparse.ArgumentParser(description=App.description)
        parser.add_argument('--version', action='version', version=about,
                            help='show version')
        parser.add_argument('-v', '--verbose', action='count',
                            default=0, help='verbose output')

        parser.add_argument('--icon')
        parser.add_argument('--lnk')
        parser.add_argument('exe', metavar='<EXE File>')

        args = parser.parse_args()
        if args.exe:
            create_shortcut(args.exe, args.lnk_path, args.icon)
        else:
            parser.print_help()


if __name__ == '__main__':
    App.run()
