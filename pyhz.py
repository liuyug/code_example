#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import os.path
import math
import struct

import pypinyin


def gen():
    offset = 0xa0
    sections = [[1, 9], [10, 15], [16, 55], [56, 87], [88, 94]]
    # positions = [1, 94]
    strings = []
    for s in range(1, 95):
        if s < sections[2][0]:
            continue
        if s > sections[2][1]:
            continue
        if s > sections[3][1]:
            continue
        for p in range(1, 95):
            if (s + offset) == 0xd7 and 0xfa <= (p + offset):
                continue
            gb_bytes = struct.pack('<2B', s + offset, p + offset)
            hz = gb_bytes.decode('gb2312')
            pys = pypinyin.pinyin(hz)[0]
            for py in pys:
                if py[:2] in ['sh', 'ch', 'zh'] or py[0] == 'r':
                    strings.append({'py': py, 'hz': hz})
    strings.sort(key=lambda x: x['py'])
    return strings


def html(strings):
    tables = []
    tables.append('''
<style>
table, th, td {border: 1px solid #96D4D4;border-collapse: collapse;}
span{display: block; text-align: center;}
</style>
    ''')
    tables.append('<table>')

    total = len(strings)
    colNum = 32
    rowNum = math.ceil(total / colNum)

    for nRow in range(rowNum):
        tables.append('<tr>')
        row_data = []
        for nCol in range(colNum):
            idx = nRow * colNum + nCol
            if idx < total:
                pyhz = strings[nRow * colNum + nCol]
                row_data.append('<td><span>%(py)s</span><span>%(hz)s</span></td>' % pyhz)
            else:
                row_data.append('<td></td>')
        tables.extend(row_data)
        tables.append('</tr>')

    tables.append('</table>')
    with open(os.path.join('build', '翘舌汉字.html'), 'wt') as f:
        f.write('\n'.join(tables))


if __name__ == '__main__':
    strings = gen()
    html(strings)
