#!/usr/bin/python3
"""0. Lockboxes
"""

def canUnlockAll(boxes):
    """documentation

    Args:
        boxes (list): is a list of lists

    Returns:
        boolean: Return True if all boxes can be opened, else return False
    """
    n = len(boxes)
    unLockBoxes = [0]

    for k, v in enumerate(boxes):
        for key in v:
            if key not in unLockBoxes and key != k:
                unLockBoxes.append(key)

    if len(unLockBoxes) == n:
        return True
    else:
        return False
