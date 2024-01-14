#!/usr/bin/python3
"""a module that unlocks boxes"""


def canUnlockAll(boxes):
    """
    A function that determines if all lockboxes can be opened.
    Args:
        boxes: is a list of lists, where each list represents a box and
        contains indices of other boxes.
    Return:
        bool: True if all lockboxes can be opened, False otherwise.
    """
    size = len(boxes)
    props = {0: 'open'}
    for idx in range(size):
        if props.get(idx) == 'open':
            print(f'check is index is open {idx}')
            keys = boxes[idx]
            for key in keys:
                if key not in props:
                    props[key] = 'open'
    return all(box in props for box in range(size))
