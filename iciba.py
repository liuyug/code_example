#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import argparse
import logging
import hashlib

import requests

logger = logging.getLogger(__name__)


class Ciba(object):
    base_url = 'http://ifanyi.iciba.com/index.php'
    prefix = '6key_web_fanyi'
    midfix = 'ifanyiweb8hc9s98e'
    # http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi&sign=27554cf4754750b2

    @classmethod
    def fy(cls, entry):
        query_data = {
            'c': 'trans',
            'm': 'fy',
            'client': '6',
            'auth_user': 'key_web_fanyi',
            'sign': '',
        }
        form_data = {
            'from': 'en',
            'to': 'auto',
            'q': entry,
        }

        encrypt_str = f'{cls.prefix}{cls.midfix}{entry}'
        sign_str = hashlib.md5(encrypt_str.encode()).hexdigest()
        print(sign_str)
        query_data['sign'] = sign_str[:16]

        res = requests.post(cls.base_url, params=query_data, data=form_data)
        res.raise_for_status()
        json_data = res.json()
        print(json_data)
        mean = json_data['content']['out']
        print(mean)


class App():
    name = 'Hello'
    description = 'Hello'
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

        parser.add_argument('word', help='word')

        args = parser.parse_args()
        level = logging.INFO - args.verbose * 10
        if level == logging.DEBUG:
            logging.basicConfig(
                level=level,
                format='%(levelname)s:%(name)s:%(message)s',
            )
        else:
            logging.basicConfig(
                level=level,
                format='%(levelname)s:%(message)s',
            )

        if args.word:
            Ciba.fy(args.word)
        else:
            parser.print_help()


if __name__ == '__main__':
    App.run()
