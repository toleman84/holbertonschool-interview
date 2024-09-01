#!/usr/bin/python3
"""0. Lockboxes
"""

def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked.

    Args:
        boxes (list): is a list of lists

    Returns:
        boolean: Return True if all boxes can be opened, else return False
    """
    n = len(boxes)
    unLockBoxes = [False] * n
    keys = boxes[0]

    for key in keys:
        if key < n and not unLockBoxes[key]:
            unLockBoxes[key] = True
            keys.extend(boxes[key])

    for i in range(1, n):
        if not unLockBoxes[i]:
            return False
    return True
