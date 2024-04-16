def canUnlockAll(boxes):
    # Initialize a set to keep track of unlocked boxes
    unlocked_boxes = set()
    
    # Function to perform DFS on the graph of boxes and keys
    def dfs(box):
        # If the box is already unlocked, return True
        if box in unlocked_boxes:
            return True
        
        # Mark the current box as unlocked
        unlocked_boxes.add(box)
        
        # Try to unlock all boxes that can be unlocked from the current box
        for key in boxes[box]:
            if not dfs(key):
                return False
        
        return True
    
    # Start DFS from the first box
    return dfs(0)

# Example usage
boxes = [
    [1, 2], # Box 0 can unlock boxes 1 and 2
    [2],     # Box 1 can unlock box 2
    []       # Box 2 has no keys
]



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