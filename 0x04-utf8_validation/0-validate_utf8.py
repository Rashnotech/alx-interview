#!/usr/bin/python3
""" a module that determines if a given set is valid UTF"""


def validUTF8(data):
    """Return True if data is a valid UTF-8"""
    try:
        bytes(data).decode('utf-8')
        return True
    except Exception:
        return False
