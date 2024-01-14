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
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True
    keys = set(boxes[0])

    def explore(box_index):
        for key in boxes[box_index]:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys.update(boxes[key])
                explore(key)
    """
    props = {0: 'open'}
    for idx in range(size):
        if props.get(idx) == 'open':
            print(f'check is index is open {idx}')
            keys = boxes[idx]
            for key in keys:
                if key not in props:
                    props[key] = 'open'
    """
    explore(0)
    return all(unlocked_boxes)
