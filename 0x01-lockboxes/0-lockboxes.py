#!/usr/bin/python3
"""
.0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    """
    num_of_boxes = len(boxes)
    visited = [False] * num_of_boxes
    visited[0] = True
    stack = [0]
    while True:
        if not stack:
            break
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < num_of_boxes and not visited[key]:
                stack.append(key)
                visited[key] = True
    return all(visited)

