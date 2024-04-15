def canUnlockAll(boxes):
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)