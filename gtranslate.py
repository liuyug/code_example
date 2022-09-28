#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import time
import os
import argparse

from googletranslate.googletranslate import main as gtranslate


def translate_text(text, verbose=False):
    class Args:
        target: str = 'zh-CN'
        query: str = ''
        host: str = 'translate.google.com'
        proxy: str = ''
        alternative: str = 'en'
        type: str = 'plain'
        synonyms: bool = False
        definitions: bool = True
        examples: bool = False
        tkk: str = ''

    Args.proxy = '127.0.0.1:1080'
    Args.query = text
    trans = []

    while True:
        result = gtranslate(Args)
        if result.startswith('^_^:'):
            break
        elif result.startswith('Errrrrrrrrror: string index out of range'):
            print('Fix:', text)
            result = text
            break
        elif result.startswith('Errrrrrrrrror:'):
            print('Error:', text, result)
            time.sleep(5)
        else:
            print(result)

    for line in result.split('\n'):
        if not line:
            continue
        elif line == '=========':
            break
        elif line == '---------':
            trans = []
            continue
        elif line.startswith('^_^:'):
            continue
        elif line.startswith('0_0:'):
            continue
        elif line.startswith('#'):
            continue
        else:
            line = '%s' % line
        trans.append(line)
    return ''.join(trans)


def translate_srt():
    cur_dir = os.getcwd()
    for root, dirs, files in os.walk(cur_dir):
        for f in files:
            if not f.endswith('.srt'):
                continue
            f = os.path.join(root, f)
            if '.en.' in f:
                en_srt = f
                zh_srt = '%s.zh.srt' % f[:-7]
            elif '.zh.' in f:
                continue
            else:
                en_srt = '%s.en.srt' % f[:-4]
                zh_srt = '%s.zh.srt' % f[:-4]
            if not os.path.exists(en_srt):
                os.rename(f, en_srt)
            print(en_srt)
            with open(en_srt, 'rt') as f_en:
                en_text = f_en.read()
                with open(zh_srt, 'wt') as f_zh:
                    count = 0
                    for line in en_text.split('\n'):
                        if count % 4 == 2:
                            line = translate_text(line)
                        f_zh.write('%s\n' % line)
                        count += 1
            time.sleep(1)


class App():
    name = 'gtranslate'
    description = 'Google Translate'
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

        parser.add_argument('--translate-text', metavar='<text>')
        parser.add_argument('--translate-srt', action='store_true')
        args = parser.parse_args()

        if args.translate_text:
            r = translate_text(args.translate_text, verbose=True)
            print(r)
        elif args.translate_srt:
            translate_srt()
        else:
            parser.print_help()


if __name__ == '__main__':
    App.run()
