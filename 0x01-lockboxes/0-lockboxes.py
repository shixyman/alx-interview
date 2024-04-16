#!/usr/bin/python3
"""
The localboxes algorithm
"""


def canUnlockAll(boxes):
    """
    @params: boxes list of lists (set representation of boxes)
    Return: True if all can be opened and the reverse is true
    """
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False

# def canUnlockAll(boxes):
#     num_boxes = len(boxes)
#     visited = [False] * num_boxes
#     visited[0] = True
#     stack = [0]

#     while stack:
#         current_box = stack.pop()

#         for key in boxes[current_box]:
#             if key < num_boxes and not visited[key]:
#                 visited[key] = True
#                 stack.append(key)

#     return all(visited)