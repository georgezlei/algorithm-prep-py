# https://github.com/georgezlei/algorithm-training-py
# Author: George Lei

import random
import collections

def topological_sort(vertices, edges):
  graph = collections.defaultdict(list)
  indegrees = [0] * vertices
  for u, v in edges:
    graph[u].append(v)
    indegrees[v] += 1

  sorted_vertices = []
  tier = [v for v in range(vertices) if indegrees[v] == 0]
  while tier:
    next_tier = []
    for u in tier:
      sorted_vertices.append(u)
      for v in graph[u]:
        indegrees[v] -= 1
        if indegrees[v] == 0:
          next_tier.append(v)
    tier = next_tier
  return sorted_vertices
    
algorithms = [
  ('Topological Sort', topological_sort)
]

# the output function used in test cases
def compareWith(arr):
  def _compare(arr1):
    if not isinstance(arr1, list):
      return False, 'expect a list, but get a {}'.format(type(arr1).__name__)

    i, j = 0, 0
    while i < len(arr) and j < len(arr1):
      set_size = len(arr[i])
      if arr[i] != set(arr1[j:j+set_size]):
        if len(set(arr1[j : j+set_size])) != set_size:
          return False, 'duplicate vertex in {}'.format(arr1[j : j+set_size])
        for f in arr1[j : j+set_size]:
          if f not in arr[i]:
            return False, '{} in wrong order'.format(f)
        return False, 'unknow reason in {}'.format(arr[j: j+set_size])
      i += 1
      j += set_size
    
    if i != len(arr):
      return False, 'vertices missing {}'.format(arr[i:])
    if j != len(arr1):
      return False, 'extra vertices {}'.format(arr1[j:])
    return True, None

  return _compare
    

test_cases = [
  {
    'name': '10 vertices',
    'in': [10, [(0, 2), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (0, 3), (4, 8)]],
    'out': compareWith([{0, 1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}])
  }
]

def generate_test_cases(number=10):
  test_cases = []
  for _ in range(number):
    vertices = [i for i in range(random.randrange(2000, 8000))]
    vertex_num = len(vertices)
    tiers = []
    edges = set()

    while vertices:
      last_tier = list(tiers[-1]) if tiers else None
      tier = set()
      tier_size = random.randint(1, len(vertices))
      while tier_size > 0:
        v = random.choice(vertices)

        vertices.remove(v)
        tier.add(v)
        tier_size -= 1
        # create an edge to v from random vertex in last tier
        if last_tier:
          u = random.choice(last_tier)
          edges.add((u, v))
      tiers.append(tier)

    # add more random edges
    lists = [list(tier) for tier in tiers]
    for j in range(vertex_num):
      i = random.randrange(0, len(tiers) - 1)
      j = random.randrange(i + 1, len(tiers))
      edges.add((random.choice(lists[i]), random.choice(lists[j])))

    test_cases.append({
      'name': 'random {} vertices'.format(vertex_num),
      'in': [vertex_num, edges],
      'out': compareWith(tiers)
    })

  return test_cases

test_cases += generate_test_cases()