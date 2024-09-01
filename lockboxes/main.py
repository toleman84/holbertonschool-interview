#!/usr/bin/python3
"""Test case for canUnlockAll function with 1000 boxes, each containing all keys."""

canUnlockAll = __import__('0-lockboxes').canUnlockAll

if __name__ == "__main__":
    # Create 1000 boxes, each containing all keys from 0 to 999
    boxes = [list(range(1000)) for _ in range(1000)]
    
    # Run the function with the test case
    result = canUnlockAll(boxes)
    
    # Print the result, should return True
    print(result)  # Expected output: True
