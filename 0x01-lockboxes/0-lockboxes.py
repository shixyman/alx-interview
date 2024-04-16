!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True

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