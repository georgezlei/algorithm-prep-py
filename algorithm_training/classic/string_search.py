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
  # preprocess t
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
  # search in s
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

def rabin_karp(s, t):
  n = len(t)
  a, a_n = 3, 3 ** n

  def rolling_hash(string):
    h, k = 0, len(string)
    for i in range(k):
      h += ord(string[i]) * a ** (k - i - 1)
    return h

  thash = rolling_hash(t)
  shash = rolling_hash(s[:n])
  if shash == thash and s[:n] == t:
    return 0
  for i in range(n, len(s)):
    shash = shash * a + ord(s[i]) - ord(s[i-n]) * a_n
    if shash == thash:
      if s[i-n+1 : i+1] == t:
        return i - n + 1
  return -1

algorithms = [
  ('Brute force', brute_force),
  ('str.find()', string_find),
  ('KMP algorithm', kmp),
  ('Rabin-Karp algorithm', rabin_karp)
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