#!/usr/bin/python3

def canUnlockAll(boxes):
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
