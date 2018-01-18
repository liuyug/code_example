#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import sys

from PyQt5 import QtWidgets, QtGui


def main():
    app = QtWidgets.QApplication(sys.argv)
    font_db = QtGui.QFontDatabase()
    print('Font Families'.center(80, '='))
    for family in font_db.families():
        print(family)
    print('=' * 80)

    print('Font Test'.center(80, '='))
    font = QtGui.QFont()
    print(font.toString())
    font.setFixedPitch(True)
    print(font.toString())

    mono_font = QtGui.QFont('Monospace')
    print(mono_font.toString())


if __name__ == '__main__':
    main()
