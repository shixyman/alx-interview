from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    
    # Set to keep track of opened boxes
    opened = set()
    opened.add(0)  # Start with box 0 (the first box is unlocked)
    
    # Queue to manage boxes to visit
    to_visit = deque([0])
    
    while to_visit:
        current_box = to_visit.popleft()
        
        # Check keys in the current box
        for key in boxes[current_box]:
            if key < n and key not in opened:  # Ensure key is within range and not already opened
                opened.add(key)
                to_visit.append(key)
    
    # Check if all boxes can be opened
    return len(opened) == n



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