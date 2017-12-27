#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView

url = 'http://www.baidu.com'


def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()

    wv = QWebEngineView(win)
    win.setCentralWidget(wv)
    win.show()

    wv.setZoomFactor(1.0)
    wv.load(QtCore.QUrl(url))

    app.exec_()


if __name__ == '__main__':
    main()
