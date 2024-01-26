#!/usr/bin/python3
""" a module that read stdin line by line and computes metrics"""
import sys
import signal


total_size = 0
line_count = 0
status_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_statistics():
    global total_size, status_code
    print('File size: {}'.format(total_size))
    for code in status_code:
        if status_code[code] > 0:
            print('{}: {}'.format(code, status_code[code]))


def signal_handler(signal, framer):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        log_info = "".join(line) 
        logs = log_info.split()
        if len(logs) < 7:
            continue
        code = int(logs[-2])
        file_size = int(logs[-1])

        total_size += file_size
        status_code[code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
