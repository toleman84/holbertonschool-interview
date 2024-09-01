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
    unLockBoxes = [0]
    keys = set(boxes[0])

    for k, v in enumerate(boxes):
        for key in v:
            if key not in unLockBoxes and key != k:
                unLockBoxes.append(key)
                keys.update(boxes[key])

    if len(unLockBoxes) == n:
        return True
    else:
        return False
