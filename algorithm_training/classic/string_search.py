# https://github.com/georgezlei/algorithm-training-py
# Author: George Lei
import random

def brute_force(s, t):
  for i in range(len(s)):
    j = 0
    while i + j < len(s) and j < len(t) and s[i+j] == t[j]:
      j += 1
    if j == len(t):
      return i
  return -1

def string_find(s, t):
  return s.find(t)

def kmp(s, t):
  next = kmp_preprocess(t)
  i = j = 0
  while i < len(s):
    if s[i] == t[j]:
      i, j = i + 1, j + 1
      if j == len(t):
        return i - j
    else:
      j = next[j]
      if j < 0:
        i, j = i + 1, j + 1
  return -1

def kmp_preprocess(t):
  next, cur = [-1], 0
  for i in range(1, len(t)):
    if t[i] == t[cur]:
      next.append(next[cur])
      cur += 1
    else:
      next.append(cur)
      cur = next[cur]
      while cur >= 0 and t[cur] != t[i]:
        cur = next[cur]
      cur += 1
  return next

def rabin_karp(s, t):
  pass

def suffix_tree(s, t):
  pass

algorithms = [
  ('Brute force', brute_force),
  ('str.find()', string_find),
  ('kmp', kmp),
]

test_cases = [
  {
    'name': 'Pattern exists',
    'in': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam molestie mollis viverra. Nam enim odio, porttitor sit amet lacus nec, imperdiet viverra neque. Suspendisse feugiat sem tellus, in cursus libero mollis quis. Etiam tincidunt sagittis pulvinar. Duis tristique maximus molestie. Vestibulum ornare luctus ligula ac vulputate. Duis cursus ex non metus posuere congue vitae nec lectus. Vivamus commodo laoreet leo vitae elementum.', 'molestie'],
    'out': 61
  },
  {
    'name': 'Pattern not exists',
    'in': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam molestie mollis viverra. Nam enim odio, porttitor sit amet lacus nec, imperdiet viverra neque. Suspendisse feugiat sem tellus, in cursus libero mollis quis. Etiam tincidunt sagittis pulvinar. Duis tristique maximus molestie. Vestibulum ornare luctus ligula ac vulputate. Duis cursus ex non metus posuere congue vitae nec lectus. Vivamus commodo laoreet leo vitae elementum.', 'aaa'],
    'out': -1
  }
]

def generate_test_cases(size=10):
  test_cases = []
  for _ in range(size):
    # generate string s
    length, s = random.randrange(10000, 50000), ''
    for i in range(length):
      s += chr(random.randrange(97, 123))
    # generate random index i and j
    i = random.randrange(0, length - 10)
    j = random.randrange(i + 1, min(i + 100, length))
    t = s[i: j]

    test_cases.append({
      'name': 'random {} length'.format(length),
      'in': [s, t],
      'out': min(i, s.find(t))
    })
  return test_cases

test_cases += generate_test_cases(100)