def canUnlockAll(boxes):
  """
  :type boxes: List[List[int]]
  :rtype: bool
  """
  visited = set([0])
  queue = [0]
  while queue:
    box = queue.pop(0)
    for key in boxes[box]:
      if key not in visited:
        visited.add(key)
        queue.append(key)
  return len(visited) == len(boxes)






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