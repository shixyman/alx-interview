from collections import deque

def canUnlockAll(boxes):
    num_boxes = len(boxes)
    visited = [False] * num_boxes  # Keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    queue = deque([0])  # Start BFS from the first box

    while queue:
        current_box = queue.popleft()

        # Check all the keys in the current box
        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

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