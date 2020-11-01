def shortest_word_edit_path(source, target, words):
  queue = [(source, 0)]
  visited = set()

  while queue:
    curr, depth = queue.pop(0)
    visited.add(curr)
    if curr == target:
      return depth
    
    for w in words:
      if w not in visited and edit_distance_is_one(curr, w):
        queue.append((w, depth + 1))
    
  return -1 

def edit_distance_is_one(curr, word):
  if len(curr) != len(word):
    return False
  
  diff_count = 0
  for i in range(len(curr)):
    if curr[i] != word[i]:
      diff_count += 1
  return diff_count == 1