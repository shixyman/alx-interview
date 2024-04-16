def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

# Example usage
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True

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