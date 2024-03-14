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
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                queue.append(key)
                visited[key] = True

    return all(visited)
