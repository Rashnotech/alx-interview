#!/usr/bin/python3
"""a module that read stdin line by line and computes metrics"""
import re
from sys import stdin, stdout

"""
total_size = 0
line_count = 0
status_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
"""


def print_statistics(total_size, status_code):
    print('File size: {}'.format(total_size))
    for code in sorted(status_code):
        if status_code[code] > 0:
            print('{}: {}'.format(code, status_code[code]))


"""
try:
    for line in sys.stdin:
        log_info = "".join(line)
        logs = log_info.split()
        if len(logs) != 9:
            continue
        code = int(logs[-2])
        file_size = int(logs[-1])

        total_size += file_size
        if code in status_code:
            status_code[code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
"""


def extract_input(input_line):
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


try:
    num = 0
    status_dict = {}
    total_size = 0
    while True:
        line = input()

        info = extract_input(line)
        num += 1
        total_size += int(info['file_size'])
        status = info['status_code']
        if status in status_dict:
            status_dict[status] += 1
        else:
            status_dict[status] = 1
        if num % 10 == 0:
            print_statistics(total_size, status_dict)
except (KeyboardInterrupt, EOFError):
    print_statistics(total_size, status_dict)
