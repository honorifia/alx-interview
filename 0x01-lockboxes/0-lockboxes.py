#!/usr/bin/python3
from collections import deque
"""
.lockboxes
"""


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True  # Mark the first box as visited
    queue = deque([0])  # Start with the first box
    boxes_checked = 1  # Keep track of the number of boxes visited

    while queue and boxes_checked < num_boxes:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)
                boxes_checked += 1

    return boxes_checked == num_boxes
